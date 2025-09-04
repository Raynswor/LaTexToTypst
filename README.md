# LaTexToTypst

A small tool to convert files from LaTeX to Typst syntax.

## Features

- Converts LaTeX documents to Typst format
- Customizable conversion rules

## Installation

Clone the repository:

```bash
git clone https://github.com/Raynswor/LaTexToTypst.git
cd LaTexToTypst/latex-to-typst
```

No dependencies are needed at the moment. 

## Usage

Run the main script to convert a LaTeX file.

```bash
python main.py --help

Examples:
  python main.py document.tex                    # Convert single file in-place
  python main.py --prefix converted_ doc.tex     # Create converted_doc.typ
  python main.py --recursive --suffix _typst .   # Convert all .tex files in current dir
  python main.py --list-rules                    # Show all conversion rules
```

## Roadmap

### ✅ Currently Supported

**Document Structure:**

- [x] Chapters (`\chapter{}` → `= Title`)
- [x] Sections (`\section{}` → `== Title`)
- [x] Subsections (`\subsection{}` → `=== Title`)
- [x] Subsubsections (`\subsubsection{}` → `==== Title`)

**Text Formatting:**

- [x] Italic text (`\textit{}`, `\emph{}` → `_text_`)
- [x] Bold text (`\textbf{}` → `*text*`)
- [x] Quoted text (`\enquote{}` → `"text"`)

**References & Citations:**

- [x] Labels (`\label{}` → `<label>`)
- [x] Cross-references (`\ref{}` → `@label`)
- [x] Citations (`\cite{}`, `\textcite{}` → `@key`)

**Special Elements:**

- [x] Footnotes (`\footnote{}` → `#footnote[text]`)
- [x] Glossary references (`\gls{}`, `\glspl{}` → `#gls("term")`)
- [x] Line breaks (`\\` → `\`)
- [x] Comments (`%` → `//`)

### 🔄 Work In Progress / Planned

**Math & Equations:**

- [ ] Inline math (`$...$` → `$...$`)
- [ ] Display math (`\begin{equation}` → `$ ... $`)

**Lists & Environments:**

- [ ] Itemize/enumerate lists
- [ ] Description lists
- [ ] Quote/quotation environments
- [ ] Verbatim/code blocks

**Tables & Figures:**

- [ ] Tabular environments
- [ ] Figure environments with captions
- [ ] Table formatting

**Advanced Formatting:**

- [ ] Font size commands (`\large`, `\small`, etc.)
- [ ] Color commands
- [ ] Spacing commands (`\vspace`, `\hspace`)

**Misc:**

- [ ] Package imports → Typst imports

## Project Structure

```text
latex-to-typst
| main.py: Main entry point for conversion
| rules.py: Conversion rules and logic
| pyproject.toml: Project configuration
```

## Contributing

Pull requests and issues are welcome!

## License

MIT
