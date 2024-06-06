import subprocess
from pathlib import Path

import typer

APP = typer.Typer()

DEFAULT_IMAGES_DIR_PATH = Path("src/images/")
DEFAULT_REPORT_PATH = Path("src/templates/report.md")
DEFAULT_SOFTWARE_DIR_PATH = Path("src/software/")
DEFAULT_PDF_OUTPUTS_DIR_PATH = Path("outputs/images/pdf/")


@APP.command()
def main(
    images_dir_path: Path = typer.Option(DEFAULT_IMAGES_DIR_PATH),
    report_path: Path = typer.Option(DEFAULT_REPORT_PATH),
    software_dir_path: Path = typer.Option(DEFAULT_SOFTWARE_DIR_PATH),
    pdf_outputs_dir_path: Path = typer.Option(DEFAULT_PDF_OUTPUTS_DIR_PATH),
):
    command = r"rg --regexp (src/images/.*)\) src/templates/report.md src/software/ --replace '$1' --only-matching --no-filename"
    command_list = command.split(" ")
    rg_result = subprocess.run(
        command_list, text=True, check=False, capture_output=True
    )

    rg_result.check_returncode()

    matched_images = rg_result.stdout.splitlines()

    pdf_outputs_dir_path.mkdir(exist_ok=True, parents=True)
    for image in matched_images:
        image_path = Path(image.strip("'"))
        output_name = image_path.with_suffix(".pdf").name
        output_path = pdf_outputs_dir_path / output_name

        print(dict(image_path=image_path, output_path=output_path))
        convert_result = subprocess.run(
            ["convert", str(image_path), str(output_path)],
            text=True,
            check=False,
            capture_output=True,
        )
        print(convert_result)
        convert_result.check_returncode()


if __name__ == "__main__":
    APP()
