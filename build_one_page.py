"""Merge the iframe-split study guide into a single one_page.html.

Reads index.html (for head/TOC/hero/footer/style) and each sections/*.html, then
emits one_page.html with all section bodies inlined and iframe routing replaced
by plain anchor scrolling.
"""
from pathlib import Path
import re

ROOT = Path(__file__).parent
SECTIONS = ROOT / "sections"

# Order matches the iframe order in index.html.
SECTION_ORDER = [
    ("ch2",            "ch2.html",            False),
    ("ch3",            "ch3.html",            False),
    ("ch4",            "ch4.html",            False),
    ("ch5",            "ch5.html",            False),
    ("ch6",            "ch6.html",            False),
    ("ch7",            "ch7.html",            False),
    ("ch8",            "ch8.html",            False),
    ("ch9",            "ch9.html",            False),
    ("practice-extra", "practice-extra.html", True),   # bg2 wrap
    ("symbols",        "symbols.html",        False),
    ("solutions",      "solutions.html",      True),   # bg2 wrap
]


def extract_body(html: str) -> str:
    """Return content between <body...> and the trailing iframe-glue script
    (inclusive of the inner content, stripped of the glue script and </body>)."""
    m = re.search(r"<body[^>]*>(.*)</body>", html, re.S | re.I)
    if not m:
        raise RuntimeError("no <body> found")
    body = m.group(1)
    # Drop the per-section <script src="iframe-glue.js?..."></script>
    body = re.sub(r'<script[^>]*\bsrc="iframe-glue\.js[^"]*"[^>]*>\s*</script>',
                  "", body, flags=re.I)
    return body.strip()


def main() -> None:
    index_html = (ROOT / "index.html").read_text(encoding="utf-8")

    # Pull the <style>...</style> block(s) from index.html — they style the shell.
    style_blocks = re.findall(r"<style>.*?</style>", index_html, re.S)
    shell_styles = "\n".join(style_blocks)

    # Pull the <header class="hero"> block.
    hero = re.search(r'<header class="hero">.*?</header>', index_html, re.S).group(0)

    # Pull the TOC nav block.
    toc = re.search(r'<nav class="toc-bar">.*?</nav>', index_html, re.S).group(0)

    # Pull the <footer> block.
    footer = re.search(r'<footer>.*?</footer>', index_html, re.S).group(0)

    # Build inlined section content.
    parts = []
    for sid, fname, bg2 in SECTION_ORDER:
        sec_html = (SECTIONS / fname).read_text(encoding="utf-8")
        body = extract_body(sec_html)
        parts.append('<div class="ch-divider"></div>')
        if bg2:
            parts.append('<div class="section-wrap-bg2">')
            parts.append(body)
            parts.append('</div>')
        else:
            parts.append(body)

    inlined = "\n\n".join(parts)

    # Simplified post-merge JS: ID assignment, dblclick ex↔sol, exercise toggles,
    # hljs highlight, smooth-scroll TOC. No iframe / postMessage logic.
    page_js = r"""
<script>
(function () {
  // Assign IDs from .sol-num / .ex-num text.
  document.querySelectorAll('.solution-item').forEach(function (item) {
    var num = item.querySelector('.sol-num');
    if (num) item.id = 'sol-' + num.textContent.trim();
  });
  document.querySelectorAll('.exercise').forEach(function (ex) {
    var num = ex.querySelector('.ex-num');
    if (num) ex.id = 'ex-' + num.textContent.trim();
  });

  function smoothScrollTo(el) {
    var rect = el.getBoundingClientRect();
    var targetY = window.scrollY + rect.top - 60;
    var startY = window.scrollY;
    var dist = targetY - startY;
    var duration = Math.min(900, Math.max(400, Math.abs(dist) / 3));
    var t0 = performance.now();
    function step(now) {
      var t = Math.min(1, (now - t0) / duration);
      var ease = t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
      window.scrollTo(0, startY + dist * ease);
      if (t < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  function flashHighlight(el) {
    el.style.outline = '2px solid var(--accent)';
    setTimeout(function () { el.style.outline = ''; }, 1500);
  }

  // Double-click exercise → jump to solution; solution → jump to exercise.
  document.querySelectorAll('.exercise').forEach(function (ex) {
    var num = ex.querySelector('.ex-num');
    if (!num) return;
    var id = num.textContent.trim();
    ex.style.cursor = 'pointer';
    ex.title = 'Double-click to jump to solution ' + id;
    ex.addEventListener('dblclick', function () {
      var t = document.getElementById('sol-' + id);
      if (t) { smoothScrollTo(t); flashHighlight(t); }
    });
  });
  document.querySelectorAll('.solution-item').forEach(function (item) {
    var num = item.querySelector('.sol-num');
    if (!num) return;
    var id = num.textContent.trim();
    item.style.cursor = 'pointer';
    item.title = 'Double-click to jump to exercise ' + id;
    item.addEventListener('dblclick', function () {
      var t = document.getElementById('ex-' + id);
      if (t) { smoothScrollTo(t); flashHighlight(t); }
    });
  });

  // Cross-section data-cross-frame / data-cross-target links → plain anchor scroll.
  document.querySelectorAll('a[data-cross-target]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      e.preventDefault();
      var t = document.getElementById(a.dataset.crossTarget);
      if (t) { smoothScrollTo(t); flashHighlight(t); }
    });
  });

  // Per-exercise done / help / review toggles in localStorage.
  function bindToggle(selector, keyPrefix, openClass, exClass) {
    document.querySelectorAll(selector).forEach(function (el) {
      var key = keyPrefix + el.dataset.num;
      var ex = el.closest('.exercise');
      try {
        if (localStorage.getItem(key) === '1') {
          el.classList.add(openClass);
          if (ex) ex.classList.add(exClass);
        }
      } catch (err) {}
      el.addEventListener('click', function (e) {
        e.stopPropagation();
        var on = el.classList.toggle(openClass);
        if (ex) ex.classList.toggle(exClass, on);
        try {
          if (on) localStorage.setItem(key, '1');
          else localStorage.removeItem(key);
        } catch (err) {}
      });
      el.addEventListener('dblclick', function (e) { e.stopPropagation(); });
    });
  }
  bindToggle('.ex-check',  'dlvg-done-',   'done',   'done');
  bindToggle('.ex-help',   'dlvg-help-',   'open',   'help');
  bindToggle('.ex-review', 'dlvg-review-', 'review', 'review');

  // Highlight Verilog <pre> blocks.
  document.addEventListener('DOMContentLoaded', function () {
    if (typeof hljs === 'undefined') return;
    var verilogRe = /\b(module|endmodule|always|assign|wire|reg|input|output|parameter|generate|endgenerate|genvar|posedge|negedge|initial|begin|end)\b/;
    document.querySelectorAll('pre').forEach(function (pre) {
      if (pre.querySelector('code')) return;
      if (!verilogRe.test(pre.textContent)) return;
      var code = document.createElement('code');
      code.className = 'language-verilog';
      code.textContent = pre.textContent;
      pre.textContent = '';
      pre.appendChild(code);
      hljs.highlightElement(code);
    });
  });

  // TOC: vertical accordion + plain anchor scroll. Sub-links with data-target,
  // data-ch/data-tier all just scroll to a known #id in this single page.
  function closeAllGroups() {
    document.querySelectorAll('.toc-group.open').forEach(function (g) { g.classList.remove('open'); });
  }
  function clearTierActive() {
    document.querySelectorAll('.toc-sub a.active').forEach(function (el) { el.classList.remove('active'); });
  }
  function clearMainActive() {
    document.querySelectorAll('.toc-main.active').forEach(function (el) { el.classList.remove('active'); });
  }

  document.querySelectorAll('.toc-main').forEach(function (main) {
    main.addEventListener('click', function (e) {
      e.preventDefault();
      var group = main.closest('.toc-group');
      var sub = group ? group.querySelector('.toc-sub') : null;
      var hasSub = sub && sub.querySelector('a');
      if (!hasSub) {
        clearMainActive(); clearTierActive(); closeAllGroups();
        main.classList.add('active');
        var href = main.getAttribute('href');
        if (href && href.startsWith('#')) {
          var t = document.getElementById(href.slice(1));
          if (t) smoothScrollTo(t);
        }
        return;
      }
      var willOpen = !group.classList.contains('open');
      closeAllGroups(); clearMainActive(); clearTierActive();
      if (willOpen) {
        group.classList.add('open');
        main.classList.add('active');
      }
    });
  });

  // tier1/tier2/tier3 sub-link: data-ch / data-tier
  // tier1 → #tier1-ch{n}, tier2/tier3 → #practice-ch{n}
  document.querySelectorAll('.toc-sub a[data-ch][data-tier]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      e.stopPropagation(); e.preventDefault();
      clearTierActive(); a.classList.add('active');
      var group = a.closest('.toc-group');
      if (group) {
        closeAllGroups(); group.classList.add('open');
        clearMainActive();
        var main = group.querySelector('.toc-main');
        if (main) main.classList.add('active');
      }
      var ch = a.dataset.ch, tier = a.dataset.tier;
      var targetId = (tier === 'tier1') ? ('tier1-' + ch) : ('practice-' + ch);
      var t = document.getElementById(targetId);
      if (t) { smoothScrollTo(t); flashHighlight(t); }
    });
  });

  // sub-link with data-target → straight anchor scroll.
  document.querySelectorAll('.toc-sub a[data-target]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      e.stopPropagation(); e.preventDefault();
      clearTierActive(); a.classList.add('active');
      var group = a.closest('.toc-group');
      if (group) {
        closeAllGroups(); group.classList.add('open');
        clearMainActive();
        var main = group.querySelector('.toc-main');
        if (main) main.classList.add('active');
      }
      var t = document.getElementById(a.dataset.target);
      if (t) { smoothScrollTo(t); flashHighlight(t); }
    });
  });
})();
</script>
""".strip()

    out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Digital Logic &amp; Verilog — Study Guide &amp; Exercises</title>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&family=JetBrains+Mono:wght@400;500;600&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body, {{
    delimiters: [
      {{left: '$$', right: '$$', display: true}},
      {{left: '$', right: '$', display: false}}
    ],
    throwOnError: false
  }});"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/styles/atom-one-light.min.css">
<script defer src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/highlight.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/languages/verilog.min.js"></script>
<link rel="stylesheet" href="sections/common.css">
{shell_styles}
</head>
<body>

{hero}

{toc}

{inlined}

{footer}

{page_js}

</body>
</html>
"""

    (ROOT / "one_page.html").write_text(out, encoding="utf-8")
    print(f"wrote one_page.html ({len(out):,} chars)")


if __name__ == "__main__":
    main()
