"""Typed report inputs; layout is maintained separately."""
from pydantic import BaseModel, ConfigDict, Field
class Record(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    code: str
    date: str
    kind: str
    title: str
    excerpt: str
    observation: str
    teaching: str
    next_step: str
    domains: tuple[int, ...]
class Counts(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    total: int = Field(ge=0)
    dated: int = Field(ge=0)
    completed: int | None = Field(default=None, ge=0)
class ReportInput(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    fields: dict[str, str]
    domains: tuple[str, ...] = Field(min_length=6, max_length=6)
    records: tuple[Record, ...] = Field(min_length=0, max_length=4)
    counts: Counts
    student_name: str = Field(min_length=1)
    class_label: str
    report_month: str = Field(pattern=r"^\d{4}-(0[1-9]|1[0-2])$")
