import os
import subprocess
from pathlib import Path
from typing import Any, Dict
import jinja2

class LaTeXReportGenerator:
    """Renders LaTeX templates with custom delimiters and compiles them to PDF."""

    def __init__(self, templates_dir: str = "templates"):
        self.templates_dir = Path(templates_dir)
        self.env = jinja2.Environment(
            block_start_string=r"\BLOCK{",
            block_end_string=r"}",
            variable_start_string=r"\VAR{",
            variable_end_string=r"}",
            comment_start_string=r"\#{",
            comment_end_string=r"}",
            line_statement_prefix="%%",
            line_comment_prefix="%#",
            trim_blocks=True,
            autoescape=False,
            loader=jinja2.FileSystemLoader(str(self.templates_dir)),
        )

    def render(self, template_name: str, data: Dict[str, Any]) -> str:
        """Render LaTeX template with given dictionary data."""
        template = self.env.get_template(template_name)
        return template.render(**data)

    def generate_tex_file(self, template_name: str, data: Dict[str, Any], output_path: str) -> Path:
        """Render and save to .tex file."""
        rendered = self.render(template_name, data)
        out_file = Path(output_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(rendered, encoding="utf-8")
        return out_file

    def compile_pdf(self, tex_file_path: str, output_dir: str = "outputs") -> Path:
        """Compile a .tex file to PDF using pdflatex."""
        tex_path = Path(tex_file_path).resolve()
        out_dir = Path(output_dir).resolve()
        out_dir.mkdir(parents=True, exist_ok=True)

        cmd = [
            "pdflatex",
            "-interaction=nonstopmode",
            f"-output-directory={str(out_dir)}",
            str(tex_path),
        ]

        try:
            result = subprocess.run(
                cmd,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            pdf_path = out_dir / f"{tex_path.stem}.pdf"
            return pdf_path
        except FileNotFoundError:
            raise RuntimeError(
                "pdflatex compiler was not found. Please install TeX Live or MiKTeX to enable PDF compilation."
            )
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"LaTeX compilation failed:\n{e.stdout}\n{e.stderr}")
