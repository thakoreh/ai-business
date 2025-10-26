# Repository Guidelines

## Project Structure & Module Organization
- Root static site. Key files:
  - `index.html` — main page (Tailwind via CDN, minimal inline JS).
  - `CNAME` — GitHub Pages custom domain. Edit only if domain changes.
- Section anchors: `#services`, `#case-study`, `#about`, `#contact`.
- If adding assets, place under `assets/` (e.g., `assets/img/`, `assets/js/`).

## Build, Test, and Development Commands
- No build step required. Open `index.html` directly in a browser, or serve locally:
  - Python: `python -m http.server 8080` then visit `http://localhost:8080`.
  - VS Code: use the Live Server extension.
- Optional checks:
  - Lighthouse (Chrome DevTools) for performance/accessibility.
  - HTML validation via W3C Validator.

## Coding Style & Naming Conventions
- HTML: 2-space indentation; prefer semantic tags (`header`, `main`, `section`, `nav`).
- Tailwind CSS: use utility-first classes; avoid inline styles except for small overrides.
- IDs/classes:
  - Section IDs kebab-case (e.g., `case-study`).
  - JS hook IDs camelCase (e.g., `navToggle`, `navMenu`, `mobileNavPanel`).
- JavaScript: keep scripts small and inline or place in `assets/js/` as `kebab-case.js`.

## Testing Guidelines
- Visual QA at common breakpoints: 360px, 768px, 1024px, 1280px.
- Verify anchor links and the mobile nav toggle work.
- Aim for Lighthouse scores ≥ 90 where practical; fix obvious a11y issues (contrast, focus states, alt text).

## Commit & Pull Request Guidelines
- Commits: imperative, concise, and scoped. Examples:
  - `feat: add case-study section`
  - `fix: correct mobile nav toggle aria state`
  - `chore: update CNAME for new domain`
- PRs should include:
  - Short description, linked issue (if any).
  - Screenshots or screen recordings for UI changes (desktop + mobile).
  - Notes on any SEO, analytics, or CNAME changes.

## Security & Configuration Tips
- Do not commit secrets. The GA tag (`G-5S07N1V724`) is public; rotate if compromised.
- Changing domains? Update `CNAME` and DNS; verify Pages is still configured.
