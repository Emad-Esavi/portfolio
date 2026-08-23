/**
 * Button ripple — GPU-friendly transform/opacity animation.
 * Skips when prefers-reduced-motion is set.
 */
(function () {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduceMotion) return;

  document.addEventListener("click", (event) => {
    const button = event.target.closest(".btn-ripple");
    if (!button) return;

    const rect = button.getBoundingClientRect();
    const wave = document.createElement("span");
    wave.className = "ripple-wave";
    wave.style.left = `${event.clientX - rect.left}px`;
    wave.style.top = `${event.clientY - rect.top}px`;
    button.appendChild(wave);

    wave.addEventListener("animationend", () => wave.remove());
  });
})();
