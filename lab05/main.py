from pathlib import Path

from tablestats import count_types, read_rows, to_csv, total_minutes


def main() -> None:
    directory = Path(__file__).resolve().parent
    path = Path(input().strip())
    if not path.is_file():
        path = directory / path

    with path.open(encoding="utf-8") as table:
        rows = read_rows(table)

    counts = count_types(rows)
    print(len(rows))
    print(len(counts))
    print(f"{total_minutes(rows, 'ошибка'):.1f}")

    with (directory / "summary.csv").open("w", encoding="utf-8", newline="") as out:
        out.write(to_csv(counts))


if __name__ == "__main__":
    main()
