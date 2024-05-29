import json
from pathlib import Path

import tomli
import typer
from jsonschema import ValidationError, validate

APP = typer.Typer()

DEFAULT_SCHEMA_JSON = Path(__file__).parent / "schema.json"


@APP.command()
def main(
    input_file: Path = typer.Argument(),
    schema_file: Path = typer.Option(DEFAULT_SCHEMA_JSON),
):
    typer.echo(f"Reading schema from {schema_file}.")
    schema = json.loads(schema_file.read_text())

    typer.echo(f"Validating toml input file {input_file}.")
    # If no exception is raised by validate(), the instance is valid.
    try:
        validate(instance=tomli.loads(input_file.read_text()), schema=schema)

    except ValidationError as error:
        message = f"{error.message} at json path {error.json_path}"
        raise ValidationError(message=message)


if __name__ == "__main__":
    APP()
