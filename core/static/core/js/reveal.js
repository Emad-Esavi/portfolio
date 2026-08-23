/**
 * Scroll reveal — adds .is-visible to [data-reveal] elements.
 * After the enter transition finishes, sets data-revealed so stagger
 * delays do not leak into hover animations.
 * Respects prefers-reduced-motion.
 */
(function () {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const nodes = document.querySelectorAll("[data-reveal]");

  if (!nodes.length) return;

  function markRevealed(el) {
    el.setAttribute("data-revealed", "");
    el.style.willChange = "auto";
  }

  function reveal(el) {
    el.classList.add("is-visible");

    const delayAttr = el.getAttribute("data-delay");
    const staggerMs = delayAttr ? Number(delayAttr) * 80 : 0;
    const durationMs = 400;
    window.setTimeout(() => markRevealed(el), staggerMs + durationMs + 50);
  }

  if (reduceMotion || !("IntersectionObserver" in window)) {
    nodes.forEach((el) => {
      el.classList.add("is-visible");
      markRevealed(el);
    });
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          reveal(entry.target);
          observer.unobserve(entry.target);
        }
      });
    },
    { rootMargin: "0px 0px -8% 0px", threshold: 0.12 }
  );

  nodes.forEach((el) => observer.observe(el));
})();
