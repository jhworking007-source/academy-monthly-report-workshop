"""Cover and closing compositions with native vector book artwork."""
from reportlab.lib.colors import HexColor
from PIL import Image
from layout import Page, LOGO, H, INK, GREY, ACCENT, ORANGE

def book(page: Page, top: float) -> None:
    """Draw layered open pages as a print-sharp brand illustration."""
    c = page.c
    for offset, fill in ((16, '#F6E1D0'), (8, '#F6C397'), (0, ORANGE)):
        c.setFillColor(HexColor(fill))
        path = c.beginPath()
        path.moveTo(65, H - top - offset)
        path.curveTo(145, H - top - 3 - offset, 233, H - top - 27 - offset, 296, H - top - 83 - offset)
        path.lineTo(296, H - top - 218 - offset)
        path.curveTo(225, H - top - 173 - offset, 148, H - top - 159 - offset, 65, H - top - 151 - offset)
        path.close()
        c.drawPath(path, fill=1, stroke=0)
        c.setFillColor(HexColor('#FFF0E3' if offset == 0 else fill))
        path = c.beginPath()
        path.moveTo(296, H - top - 83 - offset)
        path.curveTo(362, H - top - 27 - offset, 450, H - top - 3 - offset, 530, H - top - offset)
        path.lineTo(530, H - top - 151 - offset)
        path.curveTo(446, H - top - 159 - offset, 369, H - top - 173 - offset, 296, H - top - 218 - offset)
        path.close()
        c.drawPath(path, fill=1, stroke=0)
    c.setStrokeColor(HexColor('#E8AB79'))
    c.setLineWidth(0.65)
    for i in range(5):
        path = c.beginPath()
        path.moveTo(329, H - top - 105 - i * 18)
        path.curveTo(382, H - top - 76 - i * 18, 441, H - top - 61 - i * 18, 493, H - top - 54 - i * 18)
        c.drawPath(path, fill=0, stroke=1)
    page.line((296, top + 83, 296, top + 216), '#CE5900', 0.8)

def cover(page: Page, total: int, current: bool=False) -> None:
    with Image.open(LOGO) as im:
        page.c.drawImage(str(LOGO), 44, H - 68, width=140, height=140 * im.height / im.width, mask='auto')
    page.text(page.data.fields['text_001'], (470, 42, 81), (12, True, GREY))
    page.text(page.data.fields['text_002'], (442, 65, 109), (9, True, ACCENT))
    page.line((44, 105, 551, 105))
    page.text(page.data.fields['text_003'], (44, 145, 507), (12, True, ACCENT))
    headline = page.data.fields['text_004'] if not current else page.data.fields['text_092']
    page.paragraph(headline, (44, 185, 507, 153), (37, True, INK))
    page.text(page.data.fields['text_005'], (46, 326, 505), (11.5, False, GREY))
    book(page, 396)
    page.line((44, 682, 551, 682))
    page.text(page.data.fields['text_120'] if current else page.data.fields['text_120'], (44, 702, 370), (18, True, INK))
    page.text(page.data.fields['text_094'] if current else page.data.fields['text_007'], (44, 735, 370), (10.5, False, GREY))
    page.text(page.data.fields['text_008'], (468, 693, 83), (43, True, ORANGE))
    page.footer(1, total, current)

def closing(page: Page, total: int, current: bool=False) -> None:
    """Set a source-grounded principal letter in an airy portrait layout."""
    page.text(page.data.fields['text_081'], (54, 66, 487), (9, True, ACCENT))
    page.paragraph(page.data.fields['text_082'], (54, 105, 487, 56), (24, True, INK))
    page.rect((54, 175, 42, 2), ORANGE)
    page.text(page.data.fields['text_083'], (54, 214, 487), (13, True, INK))
    opening = page.data.fields['text_084']
    observation = page.data.fields['text_118'] if current else page.data.fields['text_085']
    guidance = page.data.fields['text_119'] if current else page.data.fields['text_086']
    home = page.data.fields['text_087']
    ending = page.data.fields['text_088']
    y = 255
    for text, height in ((opening, 62), (observation, 84), (guidance, 63), (home, 63), (ending, 84)):
        page.paragraph(text, (54, y, 487, height), (11.3, False, INK))
        y += height + 12
    page.text(page.data.fields['text_089'], (54, 704, 487), (10.5, False, GREY))
    page.text(page.data.fields['text_090'], (54, 733, 487), (14, True, INK))
    page.footer(total, total, current)
