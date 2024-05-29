import sys
from pathlib import Path

import pandas as pd
import tomli


def create_df(entry):
    print(entry)
    df = pd.DataFrame(entry)
    return df


def save_df(df: pd.DataFrame, key: str, output_path: Path):
    # output_dir_path.mkdir(exist_ok=True, parents=True)
    # output_path = output_dir_path / f"{key}.xlsx"
    with pd.ExcelWriter(
        path=output_path, engine="openpyxl", mode="a", if_sheet_exists="replace"
    ) as writer:
        df.to_excel(writer, sheet_name=key)
    print(output_path)


def main(input_path: Path, output_path: Path):
    data = tomli.loads(input_path.read_text())

    keys = list(data.keys())
    values = list(data.values())
    dfs = list(map(create_df, values))

    for df, key in zip(dfs, keys):
        save_df(df=df, key=key, output_path=output_path)


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
