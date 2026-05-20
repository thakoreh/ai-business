# AI Services UI Revamp Design

## Goal

Revamp `grandriverai.ca` from a warm local-consulting page into a polished AI-services studio site that feels closely aligned with `https://thakoreh.github.io/`: black canvas, direct positioning, sparse layout, subtle outline cards, proof chips, and a single orange-to-pink gradient CTA.

## Approved Direction

Use the reference site's visual language more directly:

- Near-black background with white foreground text.
- Centered hero with oversized, blunt headline copy.
- Small bordered location/status pill above the headline.
- Warm orange-to-pink gradient reserved for primary CTAs and key metric accents.
- Thin neutral borders, dark cards, rounded but restrained corners.
- Stack/tool chips to make the offer clearly read as AI services.
- Sections that prioritize services, proof, founder credibility, FAQs, and contact.

## Content Strategy

The page should keep the existing local SEO intent for Paris, Brantford, Brant County, Kitchener, Waterloo, and Cambridge, but the visible positioning should shift from "friendly AI consultant" to "builder of production AI systems."

Primary message: "AI automation that ships. Not just advice."

Primary CTA: book the existing Calendly discovery call.

## Page Structure

1. Fixed header with compact brand, anchor links, and gradient CTA.
2. Hero with local/status pill, large centered headline, short supporting copy, CTA pair, and technology chips.
3. Services section with six dark outline cards for agents, automations, SaaS/tools, LLM integrations, strategy, and fast MVP/pilot builds.
4. Proof section with shipped-system style cards and business metrics.
5. Founder/about section with Hiren's builder positioning and capability chips.
6. Process/service-area section that keeps local relevance without making the page feel provincial.
7. FAQ section using compact dark accordions.
8. Final CTA and footer.

## Constraints

- Keep this as a static `index.html` page using the existing Tailwind CDN approach.
- Keep existing metadata, analytics, Calendly URL, phone, email, and JSON-LD coverage updated to match the new visible positioning.
- Avoid decorative sci-fi dashboards, gradient blobs, and beige/sage palette.
- Preserve mobile ergonomics with a bottom sticky CTA.

## Verification

Add a small static verification script that checks for the new black-canvas theme, AI-services copy, service sections, CTA links, local SEO content, and JSON-LD. Then visually verify desktop and mobile in the browser.
