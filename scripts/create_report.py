import shutil
import subprocess
from functools import partial
from pathlib import Path
from typing import Optional

import pandas as pd
import tomli
import typer
from jinja2 import Environment, loaders, select_autoescape

APP = typer.Typer()

DEFAULT_TEMPLATES_DIR_PATH = Path("src/templates/")
DEFAULT_BIBLIOGRAPHY_PATH = Path("src/bibliography.bib")
DEFAULT_SCHEMA_TABLE_PATH = Path("src/software_schema.toml")
SECTION_TEMPLATE_NAME = "section.md"
REPORT_TEMPLATE_NAME = "report.md"
REPORT_YAML_NAME = REPORT_TEMPLATE_NAME.replace(".md", ".yaml")
DEFAULT_OUTPUT_NAME = Path(REPORT_TEMPLATE_NAME).stem
DEFAULT_OUTPUT_DIR_PATH = Path("outputs/safer2028-flop-fracture-software-report/")
DEFAULT_SOFTWARE_TOML_DIR_PATH = Path("src/software/")
DEFAULT_IMAGES_PATH = Path("src/images")
DEFAULT_CSL_PATH = Path("src/journal-of-structural-geology.csl")
DEFAULT_LATEX_TEMPLATE_PATH = DEFAULT_TEMPLATES_DIR_PATH / "pandoc_latex_template.tex"


def _render_section(
    toml_path: Path, env: Environment, section_template_name: str
) -> str:
    typer.echo(f"Reading toml input file {toml_path}.")
    toml_input = tomli.loads(toml_path.read_text())

    template = env.get_template(section_template_name)

    typer.echo("Rendering section templates")
    rendered_section = template.render(**toml_input)

    return rendered_section


def create_software_schema_table():
    # headings = ["Info", "Data", "Documentation", "Capabilities", "Remarks"]
    # descriptions = [
    #     "General links for further info on software alongside author and interface info.",
    #     "Explanation of the input and output data the software uses and outputs, respectively.",
    #     "A review of the documentation included with the software for the purposes of installation, practical use and examples",
    #     "Capabilities of the software based on source code, documentation and reference article.",
    #     "Miscellaneous additional info on the software.",
    # ]
    # assert len(headings) == len(descriptions)
    # df = pd.DataFrame(
    #     {
    #         "Heading": headings,
    #         "Description": descriptions,
    #     },
    # ).set_index("Heading")

    software_schema_from_toml = tomli.loads(DEFAULT_SCHEMA_TABLE_PATH.read_text())
    # print(software_schema_from_toml)
    df = pd.DataFrame(software_schema_from_toml["schema"]).set_index("Heading")

    return df


def format_pandoc_cmd(
    extension: str, bibliography_path: Path, output_path: Path, csl_path: Path
):
    cmd = [
        "pandoc",
        "--from",
        "markdown",
        "--to",
        extension,
        "--filter",
        "pandoc-fignos",
        "--filter",
        "pandoc-tablenos",
        "--biblio",
        str(bibliography_path),
        "--citeproc",
        "--output",
        str(output_path),
        "--toc",
        "--csl",
        str(csl_path),
        "--standalone",
    ]

    return cmd


@APP.command()
def main(
    software_toml_dir_path: Path = typer.Option(
        DEFAULT_SOFTWARE_TOML_DIR_PATH, dir_okay=True, file_okay=False
    ),
    output_dir_path: Path = typer.Option(
        DEFAULT_OUTPUT_DIR_PATH, dir_okay=True, file_okay=False
    ),
    output_name: str = typer.Option(DEFAULT_OUTPUT_NAME),
    section_template_name: str = typer.Option(SECTION_TEMPLATE_NAME),
    report_template_name: str = typer.Option(REPORT_TEMPLATE_NAME),
    report_yaml_name: str = typer.Option(REPORT_YAML_NAME),
    templates_dir_path: Path = typer.Option(DEFAULT_TEMPLATES_DIR_PATH),
    bibliography_path: Path = typer.Option(DEFAULT_BIBLIOGRAPHY_PATH),
    images_path: Path = typer.Option(DEFAULT_IMAGES_PATH),
    html_template_path: Optional[Path] = typer.Option(None),
    csl_path: Path = typer.Option(DEFAULT_CSL_PATH),
):
    env = Environment(
        loader=loaders.FileSystemLoader(templates_dir_path),
        autoescape=select_autoescape(),
    )
    render_section_partial = partial(
        _render_section, env=env, section_template_name=section_template_name
    )

    rendered_sections_map = map(
        render_section_partial, software_toml_dir_path.glob("*.toml")
    )

    software_schema_table_df = create_software_schema_table()
    software_schema_table = software_schema_table_df.to_markdown()

    rendered_report = env.get_template(report_template_name).render(
        rendered_sections=list(rendered_sections_map),
        software_schema_table=software_schema_table,
    )

    typer.echo("Formatting rendered markdown")
    result = subprocess.run(
        ["pandoc", "--from", "markdown", "--to", "markdown"],
        input=rendered_report,
        text=True,
        check=True,
        capture_output=True,
    )
    formatted_template = result.stdout

    formatted_template_with_header = "\n".join(
        [(templates_dir_path / report_yaml_name).read_text(), formatted_template]
    )

    output_dir_path.mkdir(exist_ok=True, parents=True)

    format_pandoc_cmd_with_defaults = partial(
        format_pandoc_cmd, bibliography_path=bibliography_path, csl_path=csl_path
    )

    for extension in ("pdf", "docx", "latex"):

        output_path = output_dir_path / f"{output_name}.{extension}"

        typer.echo(f"Converting markdown to {extension}")
        typer.echo(f"Writing output {extension} to {output_path}")
        cmd = format_pandoc_cmd_with_defaults(
            extension=extension, output_path=output_path
        )
        subprocess.run(
            cmd,
            input=formatted_template_with_header,
            text=True,
            check=True,
            capture_output=False,
        )

    output_path = output_dir_path / "html" / "index.html"
    output_path.parent.mkdir(exist_ok=True)

    typer.echo("Converting markdown to html")
    typer.echo(f"Writing output html to {output_path}")
    cmd = format_pandoc_cmd_with_defaults(extension="html", output_path=output_path)
    if html_template_path is not None:
        cmd.extend(["--template", str(html_template_path)])
    subprocess.run(
        cmd,
        input=formatted_template_with_header,
        text=True,
        check=True,
        capture_output=False,
    )
    images_output_path = output_path.parent / "src"
    if images_output_path.is_dir():
        shutil.rmtree(images_output_path)
    images_output_path.mkdir(exist_ok=True)
    shutil.copytree(src=images_path, dst=(images_output_path / images_path.name))


if __name__ == "__main__":
    APP()
