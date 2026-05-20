# AI Services UI Revamp Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the static Grand River AI homepage into a polished, reference-aligned AI services site.

**Architecture:** Keep the site as a single static `index.html` with Tailwind CDN configuration, inline CSS for small interactions, and inline JSON-LD. Add one lightweight shell verification script for structural and content checks.

**Tech Stack:** HTML, Tailwind CDN, vanilla JavaScript, shell verification.

---

### Task 1: Static Verification

**Files:**
- Create: `scripts/verify-site.sh`

- [ ] Add checks that fail against the current warm/sage page and pass only once the page includes the black theme, approved hero copy, AI service sections, local SEO content, Calendly CTA, and JSON-LD.
- [ ] Run `bash scripts/verify-site.sh` and confirm it fails before implementation.

### Task 2: Homepage Redesign

**Files:**
- Modify: `index.html`
- Modify: `partials/header.html`

- [ ] Replace the current warm ivory/sage styling with the approved black-canvas visual system.
- [ ] Rework the hero into centered "AI automation that ships. Not just advice." positioning.
- [ ] Add technology chips and production-service cards.
- [ ] Replace testimonial-heavy proof with shipped-system/product-style proof plus measurable outcomes.
- [ ] Keep local SEO/service-area copy and structured data aligned with the new positioning.
- [ ] Preserve mobile navigation, FAQ accordions, smooth scrolling, and sticky mobile CTA.

### Task 3: Verification

**Files:**
- Test: `scripts/verify-site.sh`

- [ ] Run `bash scripts/verify-site.sh` and confirm all checks pass.
- [ ] Serve the static page locally and inspect desktop and mobile layouts in the browser.
- [ ] Check that there are no horizontal overflow issues, blank sections, broken CTA links, or unreadable text.
