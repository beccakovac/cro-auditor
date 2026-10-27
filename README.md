# CRO Auditor

**An AI-powered conversion rate optimization (CRO) audit for any landing page.** Paste a URL and get a prioritized, page-specific report on what's stopping visitors from converting, and how to fix it.

### ▶ [Try the live app](https://cro-auditor-becca.streamlit.app)

---

## What it does

Enter a web page address, click **Run audit**, and in about a minute you get a report with:

| Section | What you get |
|---|---|
| **Snapshot** | What the page offers, who it's for, and the conversion goal it's built around |
| **What's working** | Specific strengths worth keeping |
| **Top fixes, ranked by impact** | 5–7 changes, each with the problem, why it costs conversions, the fix (including suggested copy), and an impact/effort rating |
| **Quick wins** | Small changes that take under an hour |
| **A/B test ideas** | Tests worth running, each with a clear hypothesis |

The report streams in as it's written and can be downloaded as a Markdown file.

## How it works

1. **Reads the page.** The app first does a fast, simple fetch. If the page looks empty, which happens with sites built in JavaScript frameworks like React or with many site builders, it opens the page in a headless Chromium browser. The browser scrolls through the page so lazy-loaded content and animated counters finish loading.
2. **Extracts what matters for conversion:** title and meta description, heading structure, buttons and links, form fields, image alt-text coverage, and the visible copy.
3. **Sends it to Claude** with a CRO consultant brief. Claude treats the scraped page strictly as content to review and never as instructions. It is also told not to make claims about visual design it can't see, and to flag those areas for a human check instead.

## Built with

- [Streamlit](https://streamlit.io): web interface and hosting on Streamlit Community Cloud
- [Claude API](https://www.anthropic.com/api) (Claude Opus 5.5): the audit itself
- [Playwright](https://playwright.dev/python/): headless browser for JavaScript-rendered pages
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/): HTML parsing

## Limitations

- **Text and structure only.** The audit can't see colors, layout, or images, and it doesn't measure page speed, so treat design feedback as prompts to check by eye.
- **One page at a time.** It audits the URL you enter, not the whole funnel.
- Some sites block automated visitors, and those can't be audited.

## Run it on your own computer

You'll need Python 3.10+ and a [Claude API key](https://console.anthropic.com/).

```bash
git clone https://github.com/beccakovac/cro-auditor.git
cd cro-auditor
python -m venv .venv
```

Activate the environment (`.venv\Scripts\activate` on Windows, `source .venv/bin/activate` on Mac/Linux), then:

```bash
pip install -r requirements.txt
playwright install chromium
```

Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and paste your API key between the quotes. That file is in `.gitignore`, so your key is never committed. Then start the app:

```bash
streamlit run app.py
```

---

Built by [Rebecca Kovacevich](https://www.beccakovac.com/), AI growth marketing strategist and CRO consultant.
