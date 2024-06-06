import re
from pathlib import Path

import typer

APP = typer.Typer()

DEFAULT_BIBLIOGRAPHY_PATH = Path("src/bibliography.bib")


@APP.command()
def main(
    bibliography_path: Path = typer.Option(DEFAULT_BIBLIOGRAPHY_PATH),
    output_path: Path = typer.Option(DEFAULT_BIBLIOGRAPHY_PATH),
):
    bibliography_text = bibliography_path.read_text()
    # Remove file field
    bibliography_text_sub = re.sub(
        pattern=r"\n\tfile = .*", repl=r"", string=bibliography_text
    )
    # print(bibliography_text_sub)
    output_path.write_text(bibliography_text_sub)


if __name__ == "__main__":
    APP()
