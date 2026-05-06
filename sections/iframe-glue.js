// Auto-resize iframe to content height (for the parent shell)
(function() {
  function reportHeight() {
    var h = Math.max(
      document.documentElement.scrollHeight,
      document.body.scrollHeight,
      document.documentElement.offsetHeight,
      document.body.offsetHeight
    );
    parent.postMessage({ type: 'iframe-height', name: location.pathname.split('/').pop(), height: h }, '*');
  }
  window.addEventListener('load', function() {
    reportHeight();
    setTimeout(reportHeight, 100);
    setTimeout(reportHeight, 500);
    setTimeout(reportHeight, 1500);
  });
  // Re-measure on KaTeX render and on user interaction
  if (typeof ResizeObserver !== 'undefined') {
    var ro = new ResizeObserver(function() { reportHeight(); });
    ro.observe(document.body);
  }

  // Assign IDs based on .sol-num and .ex-num content
  document.querySelectorAll('.solution-item').forEach(function(item) {
    var num = item.querySelector('.sol-num');
    if (num) item.id = 'sol-' + num.textContent.trim();
  });
  document.querySelectorAll('.exercise').forEach(function(ex) {
    var num = ex.querySelector('.ex-num');
    if (num) ex.id = 'ex-' + num.textContent.trim();
  });

  function smoothScrollTo(el) {
    var rect = el.getBoundingClientRect();
    var targetY = window.scrollY + rect.top - window.innerHeight / 2 + rect.height / 2;
    var startY = window.scrollY;
    var dist = targetY - startY;
    var duration = Math.min(900, Math.max(400, Math.abs(dist) / 3));
    var startT = performance.now();
    function step(now) {
      var t = Math.min(1, (now - startT) / duration);
      var eased = t < 0.5 ? 2*t*t : 1 - Math.pow(-2*t+2, 2)/2;
      window.scrollTo(0, startY + dist * eased);
      if (t < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  // Handle dblclick on exercise → request parent to scroll to solutions iframe and then to the right solution.
  document.querySelectorAll('.exercise').forEach(function(ex) {
    var num = ex.querySelector('.ex-num');
    if (!num) return;
    var id = num.textContent.trim();
    var localTarget = document.getElementById('sol-' + id);
    ex.style.cursor = 'pointer';
    ex.title = 'Double-click to jump to solution ' + id;
    ex.addEventListener('dblclick', function() {
      if (localTarget) {
        smoothScrollTo(localTarget);
        localTarget.style.outline = '2px solid var(--accent)';
        setTimeout(function() { localTarget.style.outline = ''; }, 1500);
      } else {
        parent.postMessage({ type: 'jump-to-solution', num: id }, '*');
      }
    });
  });

  // Same for solution-items: dblclick → jump back to exercise
  document.querySelectorAll('.solution-item').forEach(function(item) {
    var num = item.querySelector('.sol-num');
    if (!num) return;
    var id = num.textContent.trim();
    item.style.cursor = 'pointer';
    item.title = 'Double-click to jump to exercise ' + id;
    item.addEventListener('dblclick', function() {
      parent.postMessage({ type: 'jump-to-exercise', num: id }, '*');
    });
  });

  // Handle TOC sub-link clicks for symbols sub-targets (in-iframe scroll for [data-target])
  document.querySelectorAll('a[data-target]').forEach(function(a) {
    a.addEventListener('click', function(e) {
      var t = document.getElementById(a.dataset.target);
      if (t) { e.preventDefault(); smoothScrollTo(t); }
    });
  });

  // Per-exercise "done"/"review" toggles persisted in localStorage (parent's localStorage via key)
  document.querySelectorAll('.ex-check').forEach(function(el) {
    var key = 'dlvg-done-' + el.dataset.num;
    var ex  = el.closest('.exercise');
    try {
      if (localStorage.getItem(key) === '1') {
        el.classList.add('done');
        if (ex) ex.classList.add('done');
      }
    } catch (err) {}
    el.addEventListener('click', function(e) {
      e.stopPropagation();
      var done = el.classList.toggle('done');
      if (ex) ex.classList.toggle('done', done);
      try {
        if (done) localStorage.setItem(key, '1');
        else localStorage.removeItem(key);
      } catch (err) {}
    });
    el.addEventListener('dblclick', function(e) { e.stopPropagation(); });
  });

  document.querySelectorAll('.ex-help').forEach(function(el) {
    var key = 'dlvg-help-' + el.dataset.num;
    var ex  = el.closest('.exercise');
    try {
      if (localStorage.getItem(key) === '1') {
        el.classList.add('open');
        if (ex) ex.classList.add('help');
      }
    } catch (err) {}
    el.addEventListener('click', function(e) {
      e.stopPropagation();
      var on = el.classList.toggle('open');
      if (ex) ex.classList.toggle('help', on);
      try {
        if (on) localStorage.setItem(key, '1');
        else localStorage.removeItem(key);
      } catch (err) {}
    });
    el.addEventListener('dblclick', function(e) { e.stopPropagation(); });
  });

  document.querySelectorAll('.ex-review').forEach(function(el) {
    var key = 'dlvg-review-' + el.dataset.num;
    var ex  = el.closest('.exercise');
    try {
      if (localStorage.getItem(key) === '1') {
        el.classList.add('review');
        if (ex) ex.classList.add('review');
      }
    } catch (err) {}
    el.addEventListener('click', function(e) {
      e.stopPropagation();
      var on = el.classList.toggle('review');
      if (ex) ex.classList.toggle('review', on);
      try {
        if (on) localStorage.setItem(key, '1');
        else localStorage.removeItem(key);
      } catch (err) {}
    });
    el.addEventListener('dblclick', function(e) { e.stopPropagation(); });
  });

  // Highlight Verilog code blocks if hljs is available
  document.addEventListener('DOMContentLoaded', function() {
    if (typeof hljs === 'undefined') return;
    var verilogRe = /\b(module|endmodule|always|assign|wire|reg|input|output|parameter|generate|endgenerate|genvar|posedge|negedge|initial|begin|end)\b/;
    document.querySelectorAll('pre').forEach(function(pre) {
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

  // Listen for parent → iframe messages
  window.addEventListener('message', function(e) {
    var d = e.data || {};
    if (d.type === 'scroll-to-id' && d.id) {
      var el = document.getElementById(d.id);
      if (el) {
        smoothScrollTo(el);
        el.style.outline = '2px solid var(--accent)';
        setTimeout(function() { el.style.outline = ''; }, 1500);
      }
    }
    // Parent asks: where is element X inside this iframe?
    if (d.type === 'find-element' && d.id) {
      var el2 = document.getElementById(d.id);
      if (el2) {
        parent.postMessage({
          type: 'element-position',
          id: d.id,
          requestId: d.requestId,
          offsetTop: el2.offsetTop,
          offsetHeight: el2.offsetHeight
        }, '*');
      }
    }
    // Parent asks: highlight element X in this iframe
    if (d.type === 'highlight' && d.id) {
      var el3 = document.getElementById(d.id);
      if (el3) {
        el3.style.outline = '2px solid var(--accent)';
        setTimeout(function() { el3.style.outline = ''; }, 1800);
      }
    }
  });
})();
