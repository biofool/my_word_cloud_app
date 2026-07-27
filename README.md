# my_word_cloud_app

A Flask web application that generates a word cloud from keywords in a JSON quote collection and displays quotes with a searchable carousel interface.

## Overview

The app reads a JSON file of quotes (from Morihei Ueshiba's memoirs) with associated keywords, generates a word cloud image from all keywords using the `wordcloud` library, and renders an interactive web page with:
- A word cloud image visualization
- A search input for filtering quotes by keyword
- A Bootstrap carousel for browsing matching quotes

The repository also includes two standalone utility scripts:
- `CVSS.py` — Generates a CVSS v3 spider/radar chart with color-coded severity zones using matplotlib
- `ChunksOfWordDocs.py` — Splits a published Google Doc's content into HTML chunks by paragraph count using BeautifulSoup

## Prerequisites

- Python 3.8+
- System dependencies: none (uses Agg matplotlib backend for headless rendering)

## Setup

```bash
# Clone the repository
git clone https://github.com/biofool/my_word_cloud_app.git
cd my_word_cloud_app

# Install dependencies
pip install -r requirements.txt
```

Dependencies include: Flask, wordcloud, matplotlib, numpy, beautifulsoup4, requests, python-docx

## How to Run

### Word Cloud Web App

```bash
python app.py
```

Then open `http://127.0.0.1:5000/` in your browser. The app will:
1. Load quotes from `static/osensei_memoirs_quotes_8_words_escaped_pretty.json`
2. Generate a word cloud PNG from all quote keywords
3. Display the word cloud and a searchable quote carousel

### CVSS Spider Chart (standalone)

```bash
python CVSS.py
```

Displays a polar/radar chart visualizing CVSS v3 metrics with green/yellow/red severity zones.

### Google Doc Chunker (standalone)

```bash
python ChunksOfWordDocs.py
```

Fetches a published Google Doc, splits its paragraphs into chunks of 500, and saves each chunk as an HTML file (`chunk_1.html`, `chunk_2.html`, etc.).

## Project Structure

```
my_word_cloud_app/
├── app.py                  # Flask web app: word cloud generation and quote display
├── CVSS.py                 # Standalone: CVSS v3 spider chart with severity zones
├── ChunksOfWordDocs.py     # Standalone: Google Doc content chunker
├── requirements.txt        # Python dependencies
├── static/
│   ├── osensei_memoirs_quotes_8_words_escaped_pretty.json  # Quote data with keywords
│   ├── quotes.json         # Quote data (alternate)
│   ├── quotes_8_words.json # Quote data (alternate)
│   ├── wordcloud.png       # Generated word cloud image (output)
│   ├── styles.css          # Page styling
│   └── script.js           # Client-side search and carousel logic
└── templates/
    └── index.html          # Main page template with Bootstrap carousel
```

## Notes

- The word cloud is regenerated on each page load from the current quote data.
- The quote JSON files contain quotes with `keywords` arrays; the app extracts all keywords to build the word cloud.
- The CVSS values in `CVSS.py` are sample/demo values, not computed from an actual CVSS calculator.
- The Google Doc chunker uses a hardcoded published Doc URL in the example usage at the bottom of the script.
