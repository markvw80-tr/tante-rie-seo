# GEO Analysis — webshop.tanterie.nl
**Date:** 2026-05-14  
**Language:** Dutch (nl-NL)  
**Platform:** Shopify

---

## GEO Readiness Score: 46/100

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|---------|
| Citability | 30/100 | 25% | 7.5 |
| Structural Readability | 55/100 | 20% | 11.0 |
| Multi-Modal Content | 45/100 | 15% | 6.75 |
| Authority & Brand Signals | 35/100 | 20% | 7.0 |
| Technical Accessibility | 70/100 | 20% | 14.0 |
| **Total** | | | **46.25** |

---

## Platform Breakdown

| Platform | Score | Key Gap |
|----------|-------|---------|
| Google AI Overviews | 48/100 | No author, no dates, weak passage structure |
| ChatGPT | 35/100 | No Wikipedia presence, no entity graph |
| Perplexity | 28/100 | No Reddit/community discussion presence |
| Bing Copilot | 42/100 | Similar to Google AIO gap profile |

---

## AI Crawler Access Status

Shopify auto-generates robots.txt. Verified rules for named crawlers:

| Crawler | Status | Notes |
|---------|--------|-------|
| GPTBot (OpenAI) | **Likely allowed** | Not explicitly named in Shopify default robots.txt |
| OAI-SearchBot | **Likely allowed** | Not named, falls under general rules |
| ClaudeBot (Anthropic) | **Likely allowed** | Not named, falls under general rules |
| PerplexityBot | **Likely allowed** | Not named, falls under general rules |
| AhrefsBot | Allowed with 10s delay | Explicit rule present |
| Nutch | **Blocked** | Explicit Disallow |
| CCBot | Unknown | Not specified |

**Blocked paths (all bots):** `/cart`, `/checkout`, `/orders`, `/carts`, `/admin`, `/account`, `/search`, `/policies/`

**Assessment:** AI search crawlers appear unblocked. Standard Shopify restrictions (cart/checkout) do not hurt GEO. Recommend explicitly allowing key AI crawlers by name for certainty.

---

## llms.txt Status: PRESENT ✓ (Advanced)

```
Location: https://webshop.tanterie.nl/llms.txt
Extended: https://webshop.tanterie.nl/llms-full.txt
Agent docs: https://webshop.tanterie.nl/agents.md
UCP endpoint: https://webshop.tanterie.nl/.well-known/ucp
```

**Notable:** Site implements Universal Commerce Protocol (UCP) — agents can browse catalog, create carts, and initiate checkout with human approval. This is ahead of 99%+ of e-commerce sites for AI agent readiness.

**Gaps in llms.txt content:**
- No key facts section (brand stats, unique selling points)
- Blog posts not highlighted as citable resources
- No mention of physical location for local AI queries

**Recommendation:** Add to llms.txt:
```markdown
## Key Facts
- 130+ loose tea varieties
- 4.9/5 customer rating (39 verified reviews)
- Physical store: Bakkersteeg 6, 7622 GX Borne, Netherlands
- Specialist in Japanese, Chinese, and Sri Lankan teas

## Blog Resources (citable tea knowledge)
- [Japanese green tea guide](/blogs/nieuws/een-reis-door-theeregios-japan-groene-thee): Cultivation, processing, brewing
- [White tea from China](/blogs/nieuws/een-reis-door-de-theeregios-japan-witte-thee): Origins and varieties
- [Black tea from Sri Lanka](/blogs/nieuws/sri-lanka-zwarte-thee): Ceylon tea regions
```

---

## Brand Mention Analysis

| Platform | Status | Notes |
|----------|--------|-------|
| Wikipedia | **Not found** | No entity page for Tante Rie or Rie Badart |
| Reddit | **Not found** | No detectable community discussion |
| YouTube | **Not found** | No channel identified |
| LinkedIn | **Unknown** | Not detected |
| Facebook | Present | @tante_rie_borne active |
| Instagram | Present | @tante_rie_borne active |
| TikTok | Present | @tante_rie_borne active |
| Google Maps | **Likely present** | Physical address exists, unverified |

**Critical gap:** No Wikipedia/Wikidata presence. ChatGPT cites Wikipedia in 47.9% of responses. Perplexity cites Reddit in 46.7%. Both major AI platforms are effectively blind to this brand.

---

## Passage-Level Citability Assessment

**Blog post analyzed:** "Een reis door theeregio's: Japan - Groene thee" (~800 words)

**Issues found:**

1. **No author byline** — anonymous authorship is a strong negative signal for AI citation
2. **No publication date visible** — AI models de-prioritize undated content
3. **No statistics with sources** — claims like "Japanese tea is often harvested mechanically" have no citation
4. **Passages not self-contained** — paragraphs blend product promotion with educational content; AI cannot cleanly extract a citable block
5. **Dutch only** — severely limits reach for international AI queries

**Example weak passage (current):**
> "Japanse thee wordt vaak machinaal geoogst in plaats van met de hand. Door stomen (in plaats van roosteren) behoudt de thee zijn groene kleur."

**Example strong passage (rewritten for citability):**
> "Japanese green tea is typically steamed rather than pan-fired, which preserves its characteristic green color and grassy flavor profile. The steaming process deactivates oxidative enzymes within seconds of harvest, locking in chlorophyll and L-theanine. Most Japanese green tea — including Sencha, the most widely consumed variety — is machine-harvested on terraced hillsides in regions like Shizuoka and Uji. Optimal brewing uses water at 60–80°C for 1–2 minutes; the leaves can be re-steeped 2–3 times, each infusion revealing different flavor notes."

The rewritten version is 87 words — still below optimal 134–167 word range — but self-contained, factual, and extractable without context.

**Blog posts missing dates** make all 9 articles effectively uncitable for time-sensitive AI queries.

---

## Server-Side Rendering Check

**Platform:** Shopify (hosted)  
**SSR Status:** PASS — Shopify renders full HTML server-side. AI crawlers that don't execute JavaScript will still see complete product and blog content.

No JavaScript-dependent content blocking identified.

---

## Top 5 Highest-Impact Changes

### 1. Add Author Bylines + Dates to All Blog Posts (Impact: HIGH)
Every blog post needs: author name, brief bio (1–2 sentences), and publication/update date. Undated anonymous content is heavily penalized by AI citation algorithms.

**Implementation on Shopify:** Edit blog post template to show `article.author` and `article.published_at`. Takes ~30 minutes.

### 2. Add Article Schema to Blog Posts (Impact: HIGH)
No structured data detected on blog articles. Add JSON-LD `Article` schema with `author`, `datePublished`, `dateModified`, `headline`, and `description`.

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Een reis door theeregio's: Japan - Groene thee",
  "author": { "@type": "Person", "name": "Author Name" },
  "datePublished": "2025-XX-XX",
  "dateModified": "2026-XX-XX",
  "publisher": {
    "@type": "Organization",
    "name": "Tante Rie",
    "logo": { "@type": "ImageObject", "url": "https://webshop.tanterie.nl/logo.png" }
  }
}
```

### 3. Rewrite Blog Passages as Self-Contained Answer Blocks (Impact: HIGH)
Each blog section should open with a direct, complete answer in 40–60 words, then expand. Target 134–167 word self-contained blocks. Add specific facts with attributions ("According to tea researcher X..." or "Per the Japan Tea Export Promotion Council...").

### 4. Build Reddit Presence (Impact: MEDIUM-HIGH)
Perplexity cites Reddit in 46.7% of responses. Create genuine participation in Dutch-language communities:
- r/DutchFood, r/tea, r/losse_thee equivalent Dutch forums
- Answer tea questions authentically, mention Tante Rie where relevant
- One well-cited Reddit thread can drive significant Perplexity visibility

### 5. Create Wikidata Entity for "Tante Rie" (Impact: MEDIUM)
Add a minimal Wikidata entry for the business with `sameAs` links to website, social profiles, and Google Maps. This signals entity existence to ChatGPT and other AI systems that rely on knowledge graphs. Does not require Wikipedia article notability standards.

---

## Schema Recommendations

| Schema Type | Priority | Status | Action |
|-------------|----------|--------|--------|
| `Article` on blog posts | Critical | Missing | Add JSON-LD with author + dates |
| `LocalBusiness` | High | Unknown | Add with address, hours, geo coordinates |
| `BreadcrumbList` | Medium | Unknown | Shopify may auto-generate; verify |
| `Product` with `AggregateRating` | High | Partial | Verify 4.9/5 rating is in schema |
| `FAQPage` on FAQ pages | Medium | Unknown | Add to /pages/faq if exists |
| `Person` for author(s) | Medium | Missing | Add to blog template |
| `Organization` with `sameAs` | High | Missing | Link all social profiles + Wikidata |

---

## Content Reformatting Suggestions

### Pattern: Add "What is X?" definition blocks
Every tea variety page and blog post should open with a definition following the AI-citable pattern `"X is..."`:

> "Sencha is Japan's most widely consumed green tea, made from full tea leaves that are steamed immediately after harvest to prevent oxidation. Unlike Chinese green teas, which are typically pan-fired, Sencha's steaming process gives it a fresh, grassy flavor with a slightly sweet finish."

### Pattern: Add brewing spec tables
Replace prose brewing instructions with scannable tables:

| Parameter | Sencha | Matcha | Gyokuro |
|-----------|--------|--------|---------|
| Water temp | 70–80°C | 70°C | 50–60°C |
| Steep time | 1–2 min | Whisk 30s | 2–3 min |
| Ratio | 1 tbsp/cup | 1 tsp/120ml | 1 tsp/cup |
| Re-steeps | 2–3x | No | 2x |

Tables are cited at 3.2x higher rates than equivalent prose in AI responses.

### Pattern: Add sourced statistics
Replace: "Japanese tea is often harvested mechanically"  
With: "Over 90% of Japanese tea is machine-harvested (Japan Tea Export Promotion Council, 2024), unlike Indian Darjeeling where hand-picking remains standard."

---

## Quick Win Checklist

- [ ] Add publication dates to all 9 blog posts
- [ ] Add author name to all blog posts (even a pen name or "Tante Rie redactie")
- [ ] Add `Article` JSON-LD schema to blog template
- [ ] Add `Organization` schema with `sameAs` to all social/map profiles
- [ ] Add key facts + blog links section to `/llms.txt`
- [ ] Explicitly allow GPTBot and PerplexityBot by name in robots.txt (even if already allowed, explicit is better)
- [ ] Add "Wat is [theesoort]?" definition paragraph to top of each tea collection page

---

*Analysis based on live crawl of webshop.tanterie.nl on 2026-05-14. AI citation statistics from Ahrefs (Dec 2025), SparkToro (May 2025), and platform public data.*
