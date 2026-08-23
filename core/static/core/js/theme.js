(function () {
    const STORAGE_KEY = "theme";
    const DEFAULT_THEME = "noir";

    function normalizeTheme(value) {
        if (value === "light" || value === "ivory") return "ivory";
        if (value === "dark" || value === "noir") return "noir";
        return DEFAULT_THEME;
    }

    function getStoredTheme() {
        return normalizeTheme(localStorage.getItem(STORAGE_KEY));
    }

    function applyTheme(theme) {
        const next = normalizeTheme(theme);
        document.documentElement.setAttribute("data-theme", next);
        localStorage.setItem(STORAGE_KEY, next);

        const isIvory = next === "ivory";
        document.querySelectorAll(".theme-toggle").forEach((toggle) => {
            const sunIcon = toggle.querySelector('[data-theme-icon="sun"]');
            const moonIcon = toggle.querySelector('[data-theme-icon="moon"]');
            if (sunIcon) sunIcon.classList.toggle("hidden", !isIvory);
            if (moonIcon) moonIcon.classList.toggle("hidden", isIvory);
            toggle.setAttribute("aria-pressed", String(isIvory));
        });
    }

    function toggleTheme() {
        const current = normalizeTheme(
            document.documentElement.getAttribute("data-theme")
        );
        applyTheme(current === "noir" ? "ivory" : "noir");
    }

    // Apply immediately so icons match the FOUC script's theme
    applyTheme(getStoredTheme());

    document.addEventListener("click", (event) => {
        const toggle = event.target.closest(".theme-toggle");
        if (!toggle) return;
        event.preventDefault();
        toggleTheme();
    });
})();
