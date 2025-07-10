# html-to-elementor
A Python script that converts basic HTML content into Elementor-compatible JSON layout structures.

# 🔄 HTML to Elementor Converter

This Python script parses raw HTML content and converts it into a structured JSON format suitable for Elementor page builder in WordPress.

It identifies key content blocks like headings (`<h2>`, `<h3>`) and paragraphs (`<p>`), then wraps them into the Elementor schema format for sections, columns, and widgets.

## ⚙️ What It Does
- Parses HTML using `BeautifulSoup`
- Extracts heading and paragraph elements
- Converts each into Elementor widget objects
- Outputs a nested JSON structure representing a full Elementor layout

## 🧪 Example Tags Processed
- `<h2>` ➜ Converted to Elementor "Heading" widget
- `<p>` ➜ Converted to Elementor "Text Editor" widget

## 🗂️ Files
- `convert_to_Elementor.py` — main script for conversion

## 🚀 How to Use
```python
from your_script import convert_to_Elemntor

with open("example.html", "r") as file:
    html = file.read()

elementor_json = convert_to_Elemntor(html)
print(elementor_json)
