from collections.abc import Iterable


def read_rows(lines: Iterable[str]) -> list[dict]:
    header = None
    rows = []
    for line in lines:
        if not line.strip():
            continue
        fields = [field.strip() for field in line.split(",")]
        if header is None:
            header = fields
        elif len(fields) == len(header):
            rows.append(dict(zip(header, fields)))
    return rows


def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row["тип"]
        counts[kind] = counts.get(kind, 0) + 1
    return counts


def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0
    for row in rows:
        if row["тип"] == kind:
            try:
                total += float(row["минуты"].replace(",", "."))
            except ValueError:
                continue
    return round(total, 1)


def to_csv(counts: dict) -> str:
    lines = ["тип,количество"]
    for kind in sorted(counts):
        lines.append(f"{kind},{counts[kind]}")
    return "\n".join(lines) + "\n"
