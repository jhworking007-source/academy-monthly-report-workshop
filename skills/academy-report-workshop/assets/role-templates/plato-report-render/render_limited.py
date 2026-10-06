from pathlib import Path
from input_model import ReportInput
from layout import Page, INK, GREY, ACCENT, ORANGE, PALE
from bookends import cover, closing

def render(data: ReportInput, output: Path) -> None:
    p = Page(output, data)
    cover(p, 4, True)
    p.header(data.fields['text_095'], data.fields['text_096'], 2)
    p.paragraph(data.fields['text_097'], (44, 192, 507, 90), (24, True, INK))
    p.paragraph(data.fields['text_098'], (44, 311, 507, 64), (12, False, GREY))
    for x, value, label in [(44, f'{data.counts.total:02d}', data.fields['text_099']), (220, f'{data.counts.dated:02d}', data.fields['text_101']), (396, f'{data.counts.completed:02d}', data.fields['text_103'])]:
        p.text(value, (x, 418, 155), (41, False, INK))
        p.text(label, (x, 479, 155), (10, True, GREY))
    p.text(data.fields['text_104'], (44, 556, 507), (14, True, INK))
    width = 507 * data.counts.dated / data.counts.total if data.counts.total else 0
    p.rect((44, 601, 507, 14), '#D6D9DC')
    p.rect((551 - width, 601, width, 14), ORANGE)
    p.text(f'날짜 없는 기록 {data.counts.total - data.counts.dated}건', (44, 636, 330), (10, False, GREY))
    p.text(f'날짜 있음 {data.counts.dated}건', (449, 636, 102), (10, True, ACCENT))
    p.paragraph(data.fields['text_107'], (44, 700, 507, 68), (11.5, False, GREY))
    p.footer(2, 4, True)
    p.header(data.fields['text_108'], data.fields['text_109'], 3)
    p.rect((44, 184, 507, 174), PALE)
    p.text(data.fields['text_110'], (64, 204, 467), (10, True, ACCENT))
    p.paragraph(data.fields['text_111'], (64, 245, 467, 81), (24, True, INK))
    p.text(data.fields['text_112'], (44, 403, 507), (14, True, INK))
    p.paragraph(data.fields['text_113'], (44, 440, 507, 78), (18, False, INK))
    p.line((44, 548, 551, 548))
    p.text(data.fields['text_114'], (44, 573, 507), (14, True, INK))
    p.paragraph(data.fields['text_115'], (44, 612, 507, 66), (12, False, INK))
    p.text(data.fields['text_116'], (44, 711, 120), (10, True, ACCENT))
    p.paragraph(data.fields['text_117'], (184, 707, 367, 56), (11, False, GREY))
    p.footer(3, 4, True)
    closing(p, 4, True)
    p.save()
