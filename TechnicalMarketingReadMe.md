# my_word_cloud_app — Technical Marketing Summary

## One-Line Positioning

A Flask web app that visualizes quote collections as interactive word clouds with keyword-based search, plus standalone utilities for CVSS vulnerability charting and Google Doc chunking.

## Target Users / Personas

- **Content curators and educators** who want to visualize thematic keywords from a quote collection in an engaging, interactive format.
- **Security analysts** who need a quick visual representation of CVSS v3 vulnerability metrics in a radar chart format.
- **Researchers** who need to split large published Google Docs into manageable HTML chunks for processing or analysis.

## Key Features (Grounded in Code)

- **Word cloud generation**: Generates a word cloud image from keywords extracted from a JSON quote collection using the `wordcloud` library, rendered with matplotlib's headless Agg backend (`app.py`, `WordCloud().generate()`).
- **Interactive quote search**: Web interface with a search input that filters quotes by keyword, displayed in a Bootstrap carousel (`templates/index.html`, search input and carousel).
- **Flask web server**: Serves the word cloud image and quote data via a single-route Flask application (`app.py`, `@app.route('/')`).
- **CVSS v3 spider chart**: Generates a polar/radar chart with 8 CVSS metrics (Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope, Confidentiality, Integrity, Availability) and color-coded severity zones (green/yellow/red) (`CVSS.py`).
- **Google Doc chunking**: Fetches a published Google Doc via HTTP, parses paragraphs using BeautifulSoup, and splits content into chunks of configurable paragraph count saved as separate HTML files (`ChunksOfWordDocs.py`, `split_google_doc_content`).

## Technical Differentiators

- **Dynamic word cloud**: The word cloud is regenerated from live data on each page load, reflecting any changes to the quote JSON file immediately.
- **Headless rendering**: Uses matplotlib's Agg backend, allowing word cloud generation on headless servers without a display.
- **Keyword-driven visualization**: The word cloud is built specifically from curated keywords associated with each quote, not from raw text frequency, producing more meaningful visualizations.
- **Multi-purpose repository**: Combines a web app with standalone utility scripts for security visualization and document processing in a single repo.

## Use Cases

- Visualizing thematic keywords from a collection of martial arts quotes (O-Sensei's memoirs) as an interactive word cloud.
- Presenting CVSS vulnerability scores in a visual radar chart for security reports or dashboards.
- Splitting a long published Google Doc into smaller HTML chunks for batch processing or incremental analysis.

## Benefits / Value Proposition

- Turns a static JSON quote collection into an engaging visual and interactive web experience.
- The word cloud provides immediate visual insight into the most prominent themes across a quote collection.
- Standalone utilities address related but distinct needs (security visualization, document processing) without separate repositories.

## Tech Stack

- **Web framework**: Flask 2.3+
- **Word cloud**: `wordcloud` 1.9+
- **Visualization**: `matplotlib` 3.7+, `numpy`
- **Web scraping**: `beautifulsoup4`, `requests`
- **Document processing**: `python-docx`
- **Frontend**: Bootstrap 4.5, jQuery, HTML/CSS/JavaScript

## Known Limitations

- The quote JSON file path is hardcoded to `osensei_memoirs_quotes_8_words_escaped_pretty.json` in `app.py`; changing data sources requires code modification.
- The CVSS spider chart uses hardcoded sample values, not a CVSS calculator — it is a visualization template, not a scoring tool.
- The Google Doc chunker has a hardcoded example URL and runs immediately on script execution without CLI arguments.
- The word cloud is regenerated on every page load, which may be slow for large quote collections; there is no caching mechanism.
- No error handling for missing or malformed JSON data in the Flask app.
