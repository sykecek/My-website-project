/**
 * reveal.js – Reusable IntersectionObserver scroll-reveal utility.
 *
 * Usage:
 *   Add one of these classes to any element you want revealed on scroll:
 *     .reveal-up        — slides in from below
 *     .reveal-left      — slides in from the left
 *     .reveal-right     — slides in from the right
 *     .reveal-scale     — scales up from slightly smaller
 *
 *   Optional modifiers (add alongside the reveal-* class):
 *     .reveal-delay-1 … .reveal-delay-5   — stagger delays (100 ms increments)
 *
 *   When the element enters the viewport the class `.is-visible` is added,
 *   which triggers the CSS transition defined in the page stylesheet.
 *
 *   Call initReveal() after the DOM is ready (or at the bottom of <body>).
 */

(function () {
  "use strict";

  function initReveal() {
    const elements = document.querySelectorAll(
      ".reveal-up, .reveal-left, .reveal-right, .reveal-scale"
    );

    if (!elements.length) return;

    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target); // animate once
          }
        });
      },
      { threshold: 0.15 }
    );

    elements.forEach(function (el) {
      observer.observe(el);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initReveal);
  } else {
    initReveal();
  }
})();
