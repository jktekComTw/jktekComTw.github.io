import re, os, html as htmlmod

BASE = os.path.dirname(os.path.abspath(__file__))

FILES_ORDER = [
    "Cheng_Electromagnetics_2Month_Study_Plan.md",
    "# Exercise Problems from Cheng's Fi.md",
    "Ch1_Problems_Solutions.md",
    "Ch2_Problems_Solutions.md",
    "Ch3_Problems_Solutions.md",
    "Ch4_Problems_Solutions.md",
    "Ch5_Problems_Solutions.md",
    "Ch6_Problems_Solutions.md",
    "Ch7_Problems_Solutions.md",
    "Ch8_Problems_Solutions.md",
    "Ch9_Problems_Solutions.md",
    "Ch10_Problems_Solutions.md",
    "Ch11_Problems_Solutions.md",
]

# Applied in order — put longer/specific strings before shorter ones
MATH_MAP = [
    # Unit vectors with hat (before Greek letter substitution)
    ('â_ρ', r'\hat{a}_{\rho}'), ('â_φ', r'\hat{a}_{\phi}'),
    ('â_θ', r'\hat{a}_{\theta}'), ('â_r', r'\hat{a}_{r}'),
    ('â_x', r'\hat{a}_{x}'),     ('â_y', r'\hat{a}_{y}'),
    ('â_z', r'\hat{a}_{z}'),
    ('n̂',  r'\hat{n}'),          ('r̂',  r'\hat{r}'),
    ('â', r'\hat{a}'),
    # Greek uppercase — trailing space so \DeltaA doesn't merge into \DeltaA
    ('Δ', r'\Delta '), ('Σ', r'\Sigma '), ('Ω', r'\Omega '), ('Φ', r'\Phi '),
    # Greek lowercase — trailing space for same reason
    ('α', r'\alpha '), ('β', r'\beta '),  ('γ', r'\gamma '), ('δ', r'\delta '),
    ('ε', r'\varepsilon '), ('ζ', r'\zeta '), ('η', r'\eta '), ('θ', r'\theta '),
    ('λ', r'\lambda '), ('μ', r'\mu '),   ('ν', r'\nu '),   ('ξ', r'\xi '),
    ('π', r'\pi '),     ('ρ', r'\rho '),  ('σ', r'\sigma '), ('τ', r'\tau '),
    ('φ', r'\phi '),    ('χ', r'\chi '),  ('ψ', r'\psi '),   ('ω', r'\omega '),
    # Operators — trailing space so \nablaV doesn't merge
    ('×', r'\times '), ('\u00b7', r'\cdot '), ('±', r'\pm '),
    ('∇', r'\nabla '), ('∂', r'\partial '),
    ('∫', r'\int '),   ('∬', r'\iint '),       ('∮', r'\oint '),
    ('≈', r'\approx '),('≤', r'\leq '),        ('≥', r'\geq '), ('≠', r'\neq '),
    ('→', r'\to '),    ('←', r'\leftarrow '),
    ('∞', r'\infty '), ('∝', r'\propto '),
    ('⟨', r'\langle '),('⟩', r'\rangle '),
    ('✓', r'\checkmark '),
    ('\u2212', '-'),
]

# Tables for grouping consecutive super/subscript Unicode chars
_SUPER_TBL = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁻', '0123456789-')
_SUB_TBL   = str.maketrans('₀₁₂₃₄₅₆₇₈₉ₑᵥᵣₗ', '0123456789evrL')

MATH_CHARS = re.compile(
    r'[×·∇∂∫∬∮√≈≤≥≠→∞∝⟨⟩'
    r'⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉'
    r'αβγδεζηθλμνξπρστφχψωΔΣΩΦ]'
)
# Known math function names that shouldn't count as "English words"
_MATH_FUNCS = {'sinh','cosh','tanh','arccos','arcsin','arctan','sqrt','freq','arctan'}

TEXT_STARTERS = re.compile(
    r'^(Note|Using|For|At|In|Verify|Check|Also|This|The|From|By|If|Since|Where|'
    r'Compare|Physical|Practical|Alternative|Result|Total|Origin|These|Combine|'
    r'Here|Apply|So|Thus|Numerically|Alternatively|Useful|Similarly|'
    r'Therefore|Hence|Recall|Observe|Notice|Contrast|Convert|Express|'
    r'Determine|Solve|Direct|First|Second|Third|Final|General|Both|Each|'
    r'All|Proof|Confirm|Approach|Special|Recall)', re.IGNORECASE
)


def to_latex(text):
    # Combine consecutive superscript chars into one ^{...}
    text = re.sub(r'[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+',
                  lambda m: '^{' + m.group(0).translate(_SUPER_TBL) + '}', text)
    # Combine consecutive subscript chars into one _{...}
    text = re.sub(r'[₀₁₂₃₄₅₆₇₈₉ₑᵥᵣₗ]+',
                  lambda m: '_{' + m.group(0).translate(_SUB_TBL) + '}', text)
    # Generic â_X not yet in MATH_MAP
    text = re.sub(r'â_(\w+)', lambda m: r'\hat{a}_{' + m.group(1) + r'}', text)
    for src, dst in MATH_MAP:
        text = text.replace(src, dst)
    # √(expr) → \sqrt{expr}
    text = re.sub(r'√\(([^)]+)\)', r'\\sqrt{\1}', text)
    text = re.sub(r'√([\w^_{}.]+)', r'\\sqrt{\1}', text)
    return text


def is_equation_line(line):
    s = line.strip()
    if not s:
        return False
    if '=' not in s and '≈' not in s:
        return False
    if TEXT_STARTERS.match(s):
        return False
    # "Faraday's law:", "Physical meaning:", "LHS:" etc. → text label
    if re.match(r"^[A-Za-z][A-Za-z'\s]{4,}:", s):
        return False
    # Two+ English words at start → explanation sentence
    if re.match(r'^[A-Za-z]{3,}\s+[a-z]{3,}', s):
        return False
    # 2+ distinct long English words anywhere → likely prose annotation
    long_words = [w for w in re.findall(r'\b[a-z]{5,}\b', s.lower())
                  if w not in _MATH_FUNCS]
    if len(long_words) >= 2:
        return False
    # Has math content
    if MATH_CHARS.search(s) or re.search(r'[0-9]', s):
        return True
    return False


def render_solution(content):
    """Convert code-block content to a MathJax-rendered solution div."""
    lines = content.split('\n')
    out = ['<div class="sol-block">']
    for line in lines:
        s = line.strip()
        if not s:
            out.append('<div class="sol-gap"></div>')
        elif is_equation_line(line):
            latex = to_latex(s)
            out.append(f'<div class="sol-eq">\\[{htmlmod.escape(latex)}\\]</div>')
        else:
            out.append(f'<div class="sol-text">{htmlmod.escape(s)}</div>')
    out.append('</div>')
    return '\n'.join(out)


def close_list(out, list_type):
    if list_type == 'ol':
        out.append('</ol>')
    elif list_type == 'ul':
        out.append('</ul>')


def inline(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*',     r'<em>\1</em>', text)
    text = re.sub(r'`([^`]+)`',
                  lambda m: f'<code>{htmlmod.escape(m.group(1))}</code>', text)
    return text


def md_to_html(text):
    lines = text.split('\n')
    out = []
    in_code = False
    code_buf = []
    list_type = None

    i = 0
    while i < len(lines):
        line = lines[i]

        # --- code fence ---
        if line.strip().startswith('```'):
            if in_code:
                in_code = False
                out.append(render_solution('\n'.join(code_buf)))
                code_buf = []
            else:
                if list_type:
                    close_list(out, list_type)
                    list_type = None
                in_code = True
            i += 1
            continue

        if in_code:
            code_buf.append(line)
            i += 1
            continue

        # --- detect current line type for list management ---
        is_ul = bool(re.match(r'^[-*]\s+', line))
        is_ol = bool(re.match(r'^\d+\.\s+', line))

        if list_type == 'ul' and not is_ul:
            close_list(out, list_type); list_type = None
        elif list_type == 'ol' and not is_ol:
            close_list(out, list_type); list_type = None

        # --- hr ---
        if re.match(r'^---+\s*$', line):
            out.append('<hr>'); i += 1; continue

        # --- headings ---
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            level = len(m.group(1))
            content = inline(m.group(2))
            slug = re.sub(r'[^a-z0-9]+', '-',
                          re.sub(r'<[^>]+>', '', content).lower()).strip('-')
            out.append(f'<h{level} id="{slug}">{content}</h{level}>')
            i += 1; continue

        # --- unordered list ---
        if is_ul:
            m = re.match(r'^[-*]\s+(.*)', line)
            if list_type != 'ul':
                out.append('<ul>'); list_type = 'ul'
            out.append(f'<li>{inline(m.group(1))}</li>')
            i += 1; continue

        # --- ordered list ---
        if is_ol:
            m = re.match(r'^\d+\.\s+(.*)', line)
            if list_type != 'ol':
                out.append('<ol>'); list_type = 'ol'
            out.append(f'<li>{inline(m.group(1))}</li>')
            i += 1; continue

        # --- blank line ---
        if line.strip() == '':
            out.append(''); i += 1; continue

        # --- paragraph ---
        out.append(f'<p>{inline(htmlmod.escape(line))}</p>')
        i += 1

    close_list(out, list_type)
    if in_code and code_buf:
        out.append(render_solution('\n'.join(code_buf)))

    return '\n'.join(out)


def build_toc(sections):
    toc = ['<nav id="toc"><h2>Contents</h2><ol>']
    for title, anchor in sections:
        toc.append(f'<li><a href="#{anchor}">{title}</a></li>')
    toc.append('</ol></nav>')
    return '\n'.join(toc)


CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    font-family: 'Georgia', serif;
    background: #1a1a2e;
    color: #e0e0e0;
    display: flex;
    min-height: 100vh;
}
#toc {
    width: 280px; min-width: 280px;
    background: #16213e;
    padding: 24px 16px;
    position: sticky; top: 0;
    height: 100vh; overflow-y: auto;
    border-right: 1px solid #0f3460;
}
#toc h2 {
    color: #e94560; font-size: 1rem;
    text-transform: uppercase; letter-spacing: 2px;
    margin-bottom: 16px;
}
#toc ol { padding-left: 16px; }
#toc li { margin: 6px 0; }
#toc a { color: #a8b2d8; text-decoration: none; font-size: 0.85rem; }
#toc a:hover { color: #e94560; }
main { flex: 1; padding: 40px 60px; max-width: 960px; }
.section-block {
    border-bottom: 2px solid #0f3460;
    padding-bottom: 40px; margin-bottom: 40px;
}
h1 { color: #e94560; font-size: 1.8rem; margin: 24px 0 12px; }
h2 { color: #53b8ff; font-size: 1.4rem; margin: 20px 0 10px; }
h3 { color: #a8ff78; font-size: 1.1rem; margin: 16px 0 8px; }
h4, h5, h6 { color: #ffd700; margin: 12px 0 6px; }
p { line-height: 1.7; margin: 8px 0; }
hr { border: none; border-top: 1px solid #0f3460; margin: 20px 0; }
ul, ol { padding-left: 24px; margin: 8px 0; }
li { margin: 4px 0; line-height: 1.6; }

/* Solution block (replaces <pre><code>) */
.sol-block {
    background: #0d1117;
    border: 1px solid #30363d;
    border-left: 4px solid #e94560;
    border-radius: 6px;
    padding: 16px 20px;
    margin: 12px 0;
    font-size: 0.95rem;
}
.sol-text {
    font-family: 'Consolas', monospace;
    color: #8b949e;
    font-size: 0.85rem;
    padding: 1px 0;
    white-space: pre;
}
.sol-gap { height: 6px; }
.sol-eq {
    color: #c9d1d9;
    text-align: left;
    overflow-x: auto;
}
.sol-eq .MathJax { font-size: 1.05em !important; }

code {
    background: #0d1117;
    border-radius: 3px; padding: 2px 6px;
    font-family: 'Consolas', monospace;
    font-size: 0.88em; color: #79c0ff;
}
strong { color: #ffd700; }
em { color: #c3e88d; }
"""

MATHJAX_CONFIG = """
<script>
MathJax = {
  tex: {
    inlineMath: [['\\\\(','\\\\)']],
    displayMath: [['\\\\[','\\\\]']],
    packages: {'[+]': ['ams']},
    tags: 'none'
  },
  options: {
    skipHtmlTags: ['script','noscript','style','textarea','pre','code']
  },
  svg: { fontCache: 'global' }
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js" async></script>
"""

sections = []
body_parts = []

for fname in FILES_ORDER:
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        print(f"SKIP: {fname}"); continue
    with open(fpath, encoding='utf-8') as f:
        text = f.read()

    m = re.search(r'^#\s+(.+)', text, re.MULTILINE)
    title = m.group(1) if m else fname
    anchor = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    sections.append((title, anchor))

    html_body = md_to_html(text)
    body_parts.append(
        f'<section class="section-block" id="{anchor}">\n{html_body}\n</section>'
    )

toc_html  = build_toc(sections)
body_html = '\n'.join(body_parts)

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Field and Wave Electromagnetics — Cheng</title>
<style>{CSS}</style>
{MATHJAX_CONFIG}
</head>
<body>
{toc_html}
<main>
{body_html}
</main>
</body>
</html>"""

out_path = os.path.join(BASE, "electromagnetics_study_book.html")
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(page)

print(f"Written: {out_path}")
