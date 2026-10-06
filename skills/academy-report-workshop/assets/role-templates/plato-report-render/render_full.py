from pathlib import Path
from input_model import ReportInput
from layout import Page, INK, GREY, ACCENT, ORANGE, PALE
from bookends import cover, closing

def render(data: ReportInput, output: Path) -> None:
    p = Page(output, data)
    cover(p, 6)
    p.header(data.fields['text_011'], data.fields['text_012'], 2)
    p.rect((44, 183, 507, 150), PALE)
    p.rect((44, 183, 4, 150), ORANGE)
    p.text(data.fields['text_013'], (64, 203, 467), (10, True, ACCENT))
    p.paragraph(data.fields['text_014'], (64, 233, 467, 58), (18, True, INK))
    p.paragraph(data.fields['text_015'], (64, 293, 467, 26), (11.5, False, GREY))
    for y, label, body in [(367, data.fields['text_016'], data.fields['text_017']), (458, data.fields['text_018'], data.fields['text_019']), (549, data.fields['text_020'], data.fields['text_021'])]:
        p.text(label, (44, y, 120), (11, True, ACCENT))
        p.paragraph(body, (184, y - 3, 367, 63), (12, False, INK))
        p.line((44, y + 69, 551, y + 69))
    p.text(data.fields['text_022'], (44, 657, 507), (13, True, INK))
    p.text(data.fields['text_023'], (44, 693, 235), (10, True, GREY))
    p.text(data.fields['text_024'], (316, 693, 235), (10, True, ACCENT))
    p.paragraph(data.fields['text_025'], (44, 719, 235, 36), (11, False, INK))
    p.paragraph(data.fields['text_026'], (316, 719, 235, 36), (11, False, INK))
    p.footer(2, 6)
    p.header(data.fields['text_028'], data.fields['text_029'], 3)
    p.text(data.fields['text_030'], (44, 184, 507), (14, True, INK))
    xs = (273, 350, 427, 504)
    for x, r in zip(xs, data.records):
        p.text(r.date, (x - 15, 223, 45), (9, True, GREY))
    for i, domain in enumerate(data.domains):
        y = 267 + i * 35
        p.text(domain, (44, y - 8, 165), (11.5, True, INK))
        p.line((247, y, 528, y), '#ECEEF0')
        for x, r in zip(xs, data.records):
            p.dot((x, y), i in r.domains)
    p.dot((49, 480))
    p.text(data.fields['text_041'], (61, 472, 200), (9, False, ACCENT))
    p.dot((289, 480), False)
    p.text(data.fields['text_042'], (301, 472, 250), (9, False, GREY))
    p.text(data.fields['text_043'], (44, 507, 507), (9, False, GREY))
    p.line((44, 540, 551, 540))
    p.text(data.fields['text_044'], (44, 558, 507), (14, True, INK))
    rows = [data.fields['text_045'], data.fields['text_046'], data.fields['text_047'], data.fields['text_048'], data.fields['text_049'], data.fields['text_050']]
    for i, body in enumerate(rows):
        y = 595 + i * 28
        p.text(data.domains[i], (44, y, 112), (10, True, ACCENT))
        p.text(body, (171, y, 380), (10.5, False, INK))
        p.line((44, y + 22, 551, y + 22), '#EAECED')
    p.footer(3, 6)
    p.header(data.fields['text_052'], data.fields['text_053'], 4)
    p.text(data.fields['text_054'], (44, 182, 507), (11, True, GREY))
    p.rect((44, 213, 507, 112), '#F5F6F7')
    p.paragraph(data.records[0].excerpt, (64, 231, 467, 61), (14, False, INK))
    p.text(data.fields['text_056'], (64, 302, 467), (9, False, GREY))
    p.text(data.fields['text_057'], (44, 356, 507), (11, True, ACCENT))
    p.rect((44, 387, 507, 143), PALE)
    p.paragraph(data.records[2].excerpt, (64, 405, 467, 82), (14, False, INK))
    p.text(data.fields['text_059'], (64, 505, 467), (9, False, ACCENT))
    for y, label, body in [(562, data.fields['text_060'], data.fields['text_061']), (629, data.fields['text_062'], data.fields['text_063']), (696, data.fields['text_064'], data.fields['text_065'])]:
        p.text(label, (44, y, 110), (10.5, True, ACCENT))
        p.paragraph(body, (172, y - 3, 379, 54), (11.5, False, INK))
    p.footer(4, 6)
    p.header(data.fields['text_067'], data.fields['text_068'], 5)
    p.text(data.fields['text_069'], (44, 182, 507), (10, True, ACCENT))
    p.paragraph(data.fields['text_070'], (44, 218, 507, 82), (24, True, INK))
    p.line((44, 325, 551, 325))
    for y, label, body in [(349, data.fields['text_071'], data.fields['text_072']), (414, data.fields['text_073'], data.fields['text_074']), (479, data.fields['text_075'], data.fields['text_076'])]:
        p.text(label, (44, y, 112), (10.5, True, ACCENT))
        p.paragraph(body, (172, y - 3, 379, 48), (11.5, False, INK))
    p.line((44, 541, 551, 541))
    p.text(data.fields['text_077'], (44, 563, 507), (16, True, INK))
    p.rect((44, 604, 507, 78), PALE)
    p.paragraph(data.fields['text_078'], (64, 615, 467, 58), (15, True, INK))
    p.paragraph(data.fields['text_079'], (44, 703, 507, 46), (11.5, False, INK))
    p.text(data.fields['text_080'], (44, 762, 507), (8.5, False, GREY))
    p.footer(5, 6)
    closing(p, 6)
    p.save()
