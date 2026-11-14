// Testador de regex ao vivo. Usa o motor do JavaScript.
(function () {
  function esc(s) {
    return s.replace(/[&<>]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]; });
  }

  function compile(src) {
    var flags = "g";
    var m = src.match(/^\(\?([a-z]+)\)/);
    if (m) {
      src = src.slice(m[0].length);
      if (m[1].indexOf("i") >= 0) flags += "i";
      if (m[1].indexOf("m") >= 0) flags += "m";
      if (m[1].indexOf("s") >= 0) flags += "s";
    }
    return new RegExp(src, flags);
  }

  function run(box) {
    var pat = box.querySelector(".t-pattern").value;
    var text = box.querySelector(".t-text").value;
    var out = box.querySelector(".t-out");
    var re;
    try {
      re = compile(pat);
    } catch (err) {
      out.innerHTML = esc(text) + '<span class="t-status bad">Padrão inválido no JavaScript</span>';
      return;
    }
    var html = "", last = 0, count = 0, m;
    while ((m = re.exec(text)) !== null) {
      if (m[0] === "") { re.lastIndex++; continue; }
      html += esc(text.slice(last, m.index)) + "<mark>" + esc(m[0]) + "</mark>";
      last = m.index + m[0].length;
      count++;
    }
    html += esc(text.slice(last));
    var status = count
      ? '<span class="t-status ok">' + count + (count === 1 ? " trecho casou" : " trechos casaram") + "</span>"
      : '<span class="t-status">Nada casou</span>';
    out.innerHTML = html + status;
  }

  document.querySelectorAll(".tester").forEach(function (box) {
    box.querySelectorAll("input, textarea").forEach(function (el) {
      el.addEventListener("input", function () { run(box); });
    });
    run(box);
  });
})();
