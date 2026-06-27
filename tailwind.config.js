/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./**/*.html"],
  theme: {
    extend: {
      colors: {
        carbon: "#0a0a0a",
        panel: "#111111",
        line: "#262626",
        soft: "#d4d4d8",
        dim: "#a1a1aa",
        ember: "#f97316",
        rose: "#ec4899",
      },
      fontFamily: {
        sans: [
          "ui-sans-serif",
          "system-ui",
          "-apple-system",
          "BlinkMacSystemFont",
          "Segoe UI",
          "sans-serif",
        ],
      },
    },
  },
  plugins: [],
};
