# /// script
# requires-python = ">=3.11"
# dependencies = ["reportlab", "pillow", "pydantic>=2", "typer"]
# ///
# How to run: uv run generate.py CONTENT.json OUTPUT.pdf --variant full
"""Generate a report atomically from validated editable content."""
from pathlib import Path
from enum import StrEnum
from typing import assert_never
import json
import calendar
import typer
from input_model import ReportInput
from render_full import render as render_full
from render_limited import render as render_limited
class Variant(StrEnum):
    FULL = "full"
    LIMITED = "limited"
def main(content: Path, output: Path, variant: Variant = Variant.FULL) -> None:
    """Render full or limited record layouts from a supplied content file."""
    data = ReportInput.model_validate_json(content.read_text(encoding="utf-8"))
    required = set(json.loads((Path(__file__).parent / "required_fields.json").read_text()))
    missing = required - data.fields.keys()
    if missing:
        raise typer.BadParameter("Missing text fields: " + ", ".join(sorted(missing)))
    if any(i < 0 or i >= 6 for record in data.records for i in record.domains):
        raise typer.BadParameter("Observation domain index must be between 0 and 5")
    if variant == Variant.FULL and len(data.records) != 4:
        raise typer.BadParameter("Full layout requires four selected observations; use limited for insufficient records")
    if max(data.counts.dated, data.counts.completed or 0) > data.counts.total:
        raise typer.BadParameter("Record counts cannot exceed total")
    year, month = map(int, data.report_month.split("-"))
    last = calendar.monthrange(year, month)[1]
    replacements = {
        "text_001": str(year),
        "text_002": calendar.month_name[month].upper(),
        "text_006": data.student_name,
        "text_007": data.class_label,
        "text_008": f"{month:02d}",
        "text_009": f"{year}.{month:02d}",
        "text_012": f"{data.student_name} · {data.class_label} · {year}.{month:02d}.01 - {month:02d}.{last:02d}",
        "text_093": data.student_name,
        "text_096": f"{year}.{month:02d} · 이번 달 기록 확인",
        "text_120": data.student_name,
    }
    data = data.model_copy(update={"fields": data.fields | replacements})
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(".pending.pdf")
    try:
        match variant:
            case Variant.FULL:
                render_full(data, temporary)
            case Variant.LIMITED:
                render_limited(data, temporary)
            case unreachable:
                assert_never(unreachable)
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
if __name__ == "__main__":
    typer.run(main)
