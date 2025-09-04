
from dataclasses import dataclass


@dataclass
class ConversionRule:
    """Represents a single LaTeX to Typst conversion rule."""

    pattern: str
    replacement: str
    name: str
    description: str


# Conversion rules from LaTeX to Typst syntax
CONVERSION_RULES = [
    # Glossary commands
    ConversionRule(
        r"\\glspl\s*\{([^{}]+)\}",
        r'#glspl("\1")',
        "glspl",
        'Convert plural glossary references (\\glspl{term} → #glspl("term"))',
    ),
    ConversionRule(
        r"\\gls\s*\{([^{}]+)\}",
        r'#gls("\1")',
        "gls",
        'Convert singular glossary references (\\gls{term} → #gls("term"))',
    ),
    # Text formatting
    ConversionRule(
        r"\\textit\s*\{([^{}]+)\}",
        r"_\1_",
        "textit",
        "Convert italic text formatting (\\textit{text} → _text_)",
    ),
    ConversionRule(
        r"\\emph\s*\{([^{}]+)\}",
        r"_\1_",
        "emph",
        "Convert emphasized text (\\emph{text} → _text_)",
    ),
    ConversionRule(
        r"\\textbf\s*\{([^{}]+)\}",
        r"*\1*",
        "textbf",
        "Convert bold text formatting (\\textbf{text} → *text*)",
    ),
    # Document structure
    ConversionRule(
        r"\\chapter\s*\{([^{}]+)\}",
        r"= \1",
        "chapter",
        "Convert chapter headings (\\chapter{Title} → = Title)",
    ),
    ConversionRule(
        r"\\section\s*\{([^{}]+)\}",
        r"== \1",
        "section",
        "Convert section headings (\\section{Title} → == Title)",
    ),
    ConversionRule(
        r"\\subsection\s*\{([^{}]+)\}",
        r"=== \1",
        "subsection",
        "Convert subsection headings (\\subsection{Title} → === Title)",
    ),
    ConversionRule(
        r"\\subsubsection\s*\{([^{}]+)\}",
        r"==== \1",
        "subsubsection",
        "Convert subsubsection headings (\\subsubsection{Title} → ==== Title)",
    ),
    # References and labels
    ConversionRule(
        r"\\label\s*\{([^{}]+)\}",
        r"<\1>",
        "label",
        "Convert labels for cross-references (\\label{ref} → <ref>)",
    ),
    ConversionRule(
        r"\\ref\s*\{([^{}]+)\}",
        r"@\1",
        "ref",
        "Convert cross-references (\\ref{label} → @label)",
    ),
    # Citations
    ConversionRule(
        r"\\textcite\s*\{([^{}]+)\}",
        r"@\1",
        "textcite",
        "Convert textual citations (\\textcite{key} → @key)",
    ),
    ConversionRule(
        r"\\cite\s*\{([^{}]+)\}",
        r"@\1",
        "cite",
        "Convert parenthetical citations (\\cite{key} → @key)",
    ),
    # Special formatting
    ConversionRule(
        r"\\footnote\s*\{([^{}]+)\}",
        r"#footnote[\1]",
        "footnote",
        "Convert footnotes (\\footnote{text} → #footnote[text])",
    ),
    ConversionRule(
        r"\\enquote\s*\{([^{}]+)\}",
        r'"\1"',
        "enquote",
        'Convert quoted text (\\enquote{text} → "text")',
    ),
    # Special characters and syntax
    ConversionRule(
        r"\\\\",
        r"\\",
        "double backslash",
        "Convert line breaks (double backslash → single backslash)",
    ),
    ConversionRule(
        r"(?m)^%",
        r"//",
        "line comment",
        "Convert LaTeX comments (% comment → // comment)",
    ),
]