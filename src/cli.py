import argparse
import json
import sys
from pathlib import Path
from src.generator import LaTeXReportGenerator

def main():
    parser = argparse.ArgumentParser(description="Generate LaTeX reports from JSON data.")
    parser.add_argument("--data", "-d", default="data/sample_report.json", help="Path to input JSON data file")
    parser.add_argument("--template", "-t", default="report_template.tex", help="Template file name inside templates/")
    parser.add_argument("--output", "-o", default="outputs/report.tex", help="Output .tex path")
    parser.add_argument("--compile", "-c", action="store_true", help="Compile the generated .tex to PDF")

    args = parser.parse_args()

    data_path = Path(args.data)
    if not data_path.exists():
        print(f"Error: Data file '{args.data}' does not exist.", file=sys.stderr)
        sys.exit(1)

    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    generator = LaTeXReportGenerator(templates_dir="templates")
    out_tex = generator.generate_tex_file(args.template, data, args.output)
    print(f"Generated LaTeX document: {out_tex}")

    if args.compile:
        print("Compiling to PDF...")
        try:
            pdf_path = generator.compile_pdf(str(out_tex), output_dir="outputs")
            print(f"PDF successfully generated: {pdf_path}")
        except RuntimeError as e:
            print(f"Warning: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
