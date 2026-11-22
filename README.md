# LaTeX Report Generator - Refactoring & Enhancement

An extensible, automated LaTeX report generation system built with Python and Jinja2. This tool dynamically merges structured data (JSON/YAML) into clean, professional LaTeX documents and compiles them to PDF.

## 🚀 Features

- **Jinja2 LaTeX Templating**: Custom delimiters configured specifically to prevent conflicts with LaTeX syntax (`\VAR{...}`, `\BLOCK{...}`).
- **Data-Driven**: Accepts JSON or YAML structured data.
- **Auto PDF Compilation**: Automated invocation of `pdflatex` or `latexmk`.
- **Modular Architecture**: Clean separation between data parsing, template rendering, and document compilation.

## 📁 Project Structure

```text
LaTex-Report-Generator-Refactoring-and-Enhancement/
├── src/
│   ├── __init__.py
│   ├── generator.py       # Core rendering & compilation engine
│   └── cli.py             # CLI commands
├── templates/
│   └── report_template.tex # Base LaTeX template
├── data/
│   └── sample_report.json # Example input payload
├── outputs/               # Generated reports
├── requirements.txt       # Python dependencies
├── .gitignore
└── README.md
```

## 🛠️ Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Generate a Report
```bash
python -m src.cli generate --data data/sample_report.json --template templates/report_template.tex --output outputs/report.tex
```

### 3. Compile to PDF (Requires pdflatex / TeX Live / MiKTeX)
```bash
python -m src.cli generate --data data/sample_report.json --compile
```
