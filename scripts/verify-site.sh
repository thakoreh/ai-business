#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HTML="$ROOT/index.html"

require() {
  local pattern="$1"
  local label="$2"
  if ! grep -Fq "$pattern" "$HTML"; then
    echo "FAIL: missing $label"
    echo "Pattern: $pattern"
    exit 1
  fi
}

require "bg-[#0a0a0a]" "black canvas theme"
require "AI automation that ships" "approved hero headline"
require "Not just advice" "approved hero subheadline"
require "Production AI systems" "production AI positioning"
require "OpenAI API" "AI stack chip"
require "AI Agents & Chatbots" "AI agents service card"
require "AI Automations" "AI automations service card"
require "LLM Integration" "LLM service card"
require "Shipped systems" "proof section"
require "Based in Ontario" "Ontario status pill"
require "Paris, Ontario" "local SEO content"
require "Kitchener" "KWC service-area content"
require "https://calendly.com/hirenthakore/ai-automation-discovery-call" "Calendly CTA"
require "\"@type\": \"LocalBusiness\"" "LocalBusiness JSON-LD"
require "\"@type\": \"FAQPage\"" "FAQ JSON-LD"
require "motion-grid" "animated hero grid"
require "live-workflow" "live workflow preview"
require "workflow-step" "animated workflow steps"
require "data-count-to" "count-up metric hooks"
require "reveal-on-scroll" "scroll reveal hooks"
require "IntersectionObserver" "scroll animation observer"

echo "PASS: site checks passed"
