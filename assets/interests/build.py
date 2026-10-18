"""Rebuild the README images after editing interests.json. Requires Pillow for accurate text widths."""
import json
import os
from PIL import ImageFont
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "interests.json").read_text(encoding="utf-8"))
SERIF = "Georgia,'Noto Serif SC','Songti SC','SimSun',serif"
SANS = "'Segoe UI','Microsoft YaHei','Noto Sans CJK SC',sans-serif"


def text(x, y, value, size=16, color="#efece4", font=SERIF, extra=""):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{font}" font-size="{size}" {extra}>{escape(value)}</text>'


def document(width, height, title, description, body, css):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>
<style>{css}@media(prefers-reduced-motion:reduce){{.spin,.drift,.ticker{{animation:none!important}}}}</style>
{body}
</svg>\n'''


def record(mobile=False):
    w, h = (440, 397) if mobile else (920, 300)
    cx, cy, r = (102, 127, 73) if mobile else (131, 149, 87)
    body = f'<rect width="{w}" height="{h}" rx="4" fill="#141d1b"/>'
    body += '<g class="spin">'
    body += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#0b1110" stroke="#59665a"/>'
    for inset in (10, 17, 24, 31):
        body += f'<circle cx="{cx}" cy="{cy}" r="{r-inset}" fill="none" stroke="#303e34" stroke-width=".7"/>'
    body += f'<circle cx="{cx}" cy="{cy}" r="{r*.40}" fill="#bfce9f"/>'
    body += text(cx, cy - 4, "OASIS", 14, "#233021", extra='text-anchor="middle" font-weight="bold"')
    body += text(cx, cy + 12, "SIDE A · 1996", 7, "#233021", SANS, 'text-anchor="middle"')
    body += f'<circle cx="{cx}" cy="{cy}" r="3" fill="#141d1b"/></g>'
    if mobile:
        body += text(200, 120, "Don't Look", 25)
        body += text(200, 150, "Back in Anger", 25)
        body += text(202, 180, DATA["record"]["artist"], 17, "#bdcba7")
        body += text(28, 219, "On repeat", 13, "#aab9a6", SANS)
        body += text(137, 219, f'{DATA["on_repeat"]["title"]} / {DATA["on_repeat"]["artist"]}', 16)
        body += '<path d="M25 242H415V296A9 9 0 0 0 415 314V372H25V314A9 9 0 0 0 25 296Z" fill="#e9e4d6"/>'
        body += text(42, 312, DATA["musicals"][0], 46, "#293329")
        body += '<path d="M42 333H398" stroke="#aaa992" stroke-dasharray="3 4"/>'
    else:
        body += text(247, 132, "Don't Look Back", 33)
        body += text(248, 171, "in Anger", 33)
        body += text(250, 206, DATA["record"]["artist"], 18, "#bdcba7")
        body += '<path d="M625 66H890V147A10 10 0 0 0 890 167V233H625V167A10 10 0 0 0 625 147Z" fill="#e9e4d6"/>'
        body += text(647, 154, DATA["musicals"][0], 43, "#293329")
        body += '<path d="M647 194H869" stroke="#aaa992" stroke-dasharray="3 4"/>'
        body += '<path d="M28 251H892" stroke="#37433a"/>'
        body += text(30, 279, "On repeat", 13, "#aab9a6", SANS)
        body += text(149, 280, f'{DATA["on_repeat"]["title"]} / {DATA["on_repeat"]["artist"]}', 18)
    css = f'.spin{{transform-origin:{cx}px {cy}px;animation:turn 28s linear infinite}}@keyframes turn{{to{{transform:rotate(360deg)}}}}'
    description = f'{DATA["record"]["artist"]} — {DATA["record"]["title"]}；最近单曲循环：借过 — 印子月；音乐剧：' + '、'.join(DATA["musicals"])
    return document(w, h, "唱片与票根", description, body, css)


def cloud(mobile=False):
    w, h = (440, 725) if mobile else (920, 590)
    key = "mobile" if mobile else "desktop"
    body = f'<rect width="{w}" height="{h}" rx="4" fill="#f2f1eb"/>'
    body += text(28, 34, DATA["note"], 18, "#435b3e", SANS, 'font-weight="600"')
    body += f'<path d="M28 49H{w-28}" stroke="#cdd2c6"/>'
    rows = DATA['flow_rows'][key]
    styles = []
    for row_index, row in enumerate(rows):
        gap = 25 if mobile else 38
        widths = [ImageFont.truetype(os.environ.get('INTERESTS_FONT', 'C:/Windows/Fonts/georgia.ttf'), size).getlength(label) for label, size in row]
        total = sum(widths) + gap * (len(row)-1)
        travel = min(66 if mobile else 100, (w-total)/2-30)
        assert travel > 8, (key, row, total)
        x = (w-total)/2
        y = (105 + row_index*53) if mobile else (118 + row_index*66)
        duration = 12 + row_index % 3
        styles.append(f'@keyframes lane{row_index}{{0%,100%{{transform:translate({-travel:.1f}px,0)}}25%{{transform:translate(0,-6px)}}50%{{transform:translate({travel:.1f}px,0)}}75%{{transform:translate(0,6px)}}}}')
        body += f'<g class="lane" style="animation:lane{row_index} {duration}s linear infinite;animation-delay:-{row_index*2.4}s">'
        for j, ((label,size), width) in enumerate(zip(row,widths)):
            color = '#45523e' if size < 20 else '#263b2b'
            extra = 'font-style="italic"' if label == 'Komm, süsser Tod' else ''
            body += f'<g class="drift" style="animation-delay:-{row_index+j*1.3}s">'
            body += text(round(x,2),y + (j%2)*5,label,size,color,extra=extra)+'</g>'
            x += width + gap
        body += '</g>'
    y = h - 27
    lead = DATA["attitude"]["lead"]
    tail = DATA["attitude"]["tail"]
    start = 169 if mobile else 190
    body += f'<path d="M28 {y-25}H{w-28}" stroke="#cdd2c6"/>'
    body += text(28, y, lead, 13, "#506245", SANS)
    body += f'<defs><clipPath id="strip"><rect x="{start}" y="{y-18}" width="{w-start-28}" height="25"/></clipPath></defs>'
    body += '<g clip-path="url(#strip)"><g class="ticker">'
    for offset in (0, 1080):
        body += text(start + offset, y, tail, 12, "#7d8976", SANS, 'textLength="1040" lengthAdjust="spacing"')
    body += '</g></g>'
    css = ''.join(styles) + """.drift{animation:tone 6s ease-in-out infinite}
@keyframes tone{0%,100%{opacity:.65}50%{opacity:1}}
.ticker{animation:flow 66s linear infinite}@keyframes flow{to{transform:translateX(-1080px)}}
@media(prefers-reduced-motion:reduce){.lane,.drift{animation:none!important;opacity:1;transform:none}}"""
    description = DATA["note"] + '：' + '、'.join(x["text"] for x in DATA["words"]) + '。' + lead + tail
    return document(w, h, "最近提到", description, body, css)


if __name__ == "__main__":
    for name, builder in (("records", record), ("words", cloud)):
        for mobile in (False, True):
            filename = f'{name}{"-mobile" if mobile else ""}.svg'
            (HERE / filename).write_text(builder(mobile), encoding="utf-8")
            print(filename)
