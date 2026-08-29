/**
 * Zoltan Gero brand system  Tailwind preset
 * For future Tailwind / shadcn projects only. PDT does not use this.
 *
 * Usage:
 *   // tailwind.config.js
 *   module.exports = { presets: [require("../design-system/tailwind-preset")] }
 *
 * Pair with the :root / .dark custom-property blocks from tokens.css as your
 * globals.css so bg-primary etc. resolve to the same values everywhere.
 */
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#EBF3FE", 100: "#D6E6FD", 200: "#B0CEFB", 300: "#82B0F7",
          400: "#4F8DF0", 500: "#1E7CE8", 600: "#1663C6", 700: "#144F9F",
          800: "#163F7B", 900: "#15355F", 950: "#0E2038",
        },
        accent: {
          50: "#E4F5EA", 100: "#BFE8CC", 200: "#8DD5A6", 300: "#56BE7B",
          400: "#24A957", 500: "#12A150", 600: "#0E8542", 700: "#0C6A36",
          800: "#0C5430", 900: "#0A4228",
        },
        neutral: {
          0: "#FFFFFF", 50: "#F6F8FC", 100: "#EDF1F7", 200: "#E0E6F0",
          300: "#CAD3E1", 400: "#97A3B8", 500: "#6A7688", 600: "#4C5768",
          700: "#333D4C", 800: "#1E2733", 900: "#131A24",
        },
        // shadcn-style role tokens, backed by CSS variables from tokens.css
        background: "var(--background)",
        foreground: "var(--foreground)",
        surface: "var(--surface)",
        muted: { DEFAULT: "var(--muted)", foreground: "var(--muted-foreground)" },
        primary: { DEFAULT: "var(--primary)", foreground: "var(--primary-foreground)" },
        secondary: { DEFAULT: "var(--secondary)", foreground: "var(--secondary-foreground)" },
        border: "var(--border)",
        input: "var(--input)",
        ring: "var(--ring)",
        success: "#0B7A3E", warning: "#E5A400", danger: "#E5484D",
      },
      fontFamily: {
        sans: ['"Open Sans"', '"Segoe UI"', "system-ui", "sans-serif"],
        display: ['"Open Sans"', '"Segoe UI"', "system-ui", "sans-serif"],
        mono: ['"Geist Mono"', "ui-monospace", "Menlo", "monospace"],
      },
      fontSize: {
        xs:  ["0.8125rem",{ lineHeight: "1.125rem" }],
        sm:  ["0.9375rem",{ lineHeight: "1.375rem" }],
        base:["1.125rem", { lineHeight: "1.75rem" }],
        lg:  ["1.25rem",  { lineHeight: "1.85rem",  letterSpacing: "-0.006em" }],
        xl:  ["1.375rem", { lineHeight: "1.95rem",  letterSpacing: "-0.01em" }],
        "2xl":["1.625rem",{ lineHeight: "2.1rem",   letterSpacing: "-0.012em" }],
        "3xl":["2rem",    { lineHeight: "2.4rem",   letterSpacing: "-0.016em" }],
        "4xl":["2.5rem",  { lineHeight: "2.85rem",  letterSpacing: "-0.02em" }],
        "5xl":["3.125rem",{ lineHeight: "3.35rem",  letterSpacing: "-0.022em" }],
        "6xl":["3.875rem",{ lineHeight: "4rem",     letterSpacing: "-0.026em" }],
        "7xl":["4.625rem",{ lineHeight: "4.75rem",  letterSpacing: "-0.03em" }],
      },
      borderRadius: {
        sm: "6px", md: "10px", lg: "12px", xl: "16px", "2xl": "24px",
      },
      boxShadow: {
        xs: "0 1px 2px rgba(14,32,56,0.06)",
        sm: "0 1px 3px rgba(14,32,56,0.08), 0 1px 2px rgba(14,32,56,0.04)",
        md: "0 4px 12px rgba(14,32,56,0.08)",
        lg: "0 12px 28px rgba(14,32,56,0.12)",
        cta: "0 6px 20px rgba(18,161,80,0.30)",
      },
      transitionTimingFunction: {
        standard: "cubic-bezier(0.4,0,0.2,1)",
        out: "cubic-bezier(0,0,0.2,1)",
      },
      keyframes: {
        "cta-halo": {
          "0%":   { boxShadow: "0 0 0 0 rgba(18,161,80,0.45)" },
          "70%":  { boxShadow: "0 0 0 14px rgba(18,161,80,0)" },
          "100%": { boxShadow: "0 0 0 0 rgba(18,161,80,0)" },
        },
        "cta-breathe": {
          "0%,100%": { transform: "scale(1)" },
          "50%":     { transform: "scale(1.025)" },
        },
      },
      animation: {
        "cta-halo": "cta-halo 2.4s cubic-bezier(0,0,0.2,1) infinite",
        "cta-breathe": "cta-breathe 3s cubic-bezier(0.4,0,0.2,1) infinite",
      },
    },
  },
};
