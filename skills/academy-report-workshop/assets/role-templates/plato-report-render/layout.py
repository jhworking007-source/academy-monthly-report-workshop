"""Portrait report primitives with bounded, left-aligned typography."""
from pathlib import Path
from input_model import ReportInput
from typing import Final
from xml.sax.saxutils import escape
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
W: Final = 595.276
H: Final = 841.89
ORANGE: Final = '#ED6D00'
ACCENT: Final = '#A94800'
INK: Final = '#242629'
GREY: Final = '#676B70'
PALE: Final = '#FFF6EF'
LINE: Final = '#E0E2E4'
ROOT: Final = Path(__file__).resolve().parent
LOGO: Final = ROOT / 'assets/logo.png'
pdfmetrics.registerFont(TTFont('KR', 'C:/Windows/Fonts/malgun.ttf'))
pdfmetrics.registerFont(TTFont('KRB', 'C:/Windows/Fonts/malgunbd.ttf'))

class Page:
    """Mutable drawing accumulator; text bounds are checked at authoring time."""

    def __init__(self, path: Path, data: ReportInput) -> None:
        self.data = data
        self.c = Canvas(str(path), pagesize=(W, H))
        self.c.setTitle('플라톤 월간 독서·논술 리포트')
        self.c.setAuthor('플라톤 독서논술')

    def text(self, content: str, bounds: tuple[float, float, float], style: tuple[float, bool, str]=(11, False, INK)) -> None:
        x, y, w = bounds
        size, bold, color = style
        font = 'KRB' if bold else 'KR'
        if not pdfmetrics.stringWidth(content, font, size) <= w:
            raise OverflowError(str((content, w)))
        self.c.setFillColor(HexColor(color))
        self.c.setFont(font, size)
        self.c.drawString(x, H - y - size, content)

    def paragraph(self, content: str, bounds: tuple[float, float, float, float], style: tuple[float, bool, str]=(11.5, False, INK)) -> None:
        x, y, w, max_h = bounds
        size, bold, color = style
        p = Paragraph(escape(content).replace('\n', '<br/>'), ParagraphStyle('p', fontName='KRB' if bold else 'KR', fontSize=size, leading=size * 1.55, textColor=HexColor(color), wordWrap='LTR', splitLongWords=False, alignment=0))
        _, h = p.wrap(w, max_h)
        if not h <= max_h:
            raise OverflowError(str((content, h, max_h)))
        p.drawOn(self.c, x, H - y - h)

    def line(self, ends: tuple[float, float, float, float], color: str=LINE, width: float=0.6) -> None:
        x, y, x2, y2 = ends
        self.c.setStrokeColor(HexColor(color))
        self.c.setLineWidth(width)
        self.c.line(x, H - y, x2, H - y2)

    def rect(self, bounds: tuple[float, float, float, float], color: str=PALE) -> None:
        x, y, w, h = bounds
        self.c.setFillColor(HexColor(color))
        self.c.rect(x, H - y - h, w, h, stroke=0, fill=1)

    def dot(self, xy: tuple[float, float], filled: bool=True) -> None:
        x, y = xy
        self.c.setFillColor(HexColor(ORANGE if filled else '#E9EBED'))
        self.c.circle(x, H - y, 4.5, stroke=0, fill=1)

    def header(self, title: str, subtitle: str, page: int) -> None:
        with Image.open(LOGO) as im:
            self.c.drawImage(str(LOGO), 44, H - 49, width=111, height=111 * im.height / im.width, mask='auto')
        self.text(self.data.fields['text_009'], (487, 31, 65), (10, True, GREY))
        self.line((44, 72, 551, 72))
        self.text(f'{page:02d}', (44, 102, 28), (13, True, ACCENT))
        self.text(title, (83, 96, 468), (24, True, INK))
        self.text(subtitle, (83, 136, 468), (9.5, False, GREY))

    def footer(self, page: int, total: int, current: bool=False) -> None:
        self.line((44, 786, 551, 786))
        note = self.data.fields['text_003']
        self.text(note, (44, 801, 456), (7.5, False, GREY))
        self.text(f'{page:02d} / {total:02d}', (509, 801, 42), (8, True, GREY))
        self.c.showPage()

    def save(self) -> None:
        self.c.save()
