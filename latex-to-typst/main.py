#!/usr/bin/env python3
"""
LaTeX to Typst Converter

A tool to convert LaTeX documents to Typst markup by applying a set of
transformation rules. Supports processing single files or entire directories
with options for in-place editing or custom output naming.
"""

import argparse
import re
from pathlib import Path
from rules import CONVERSION_RULES


def transform(text: str, verbose: bool = True) -> str:
    """
    Apply all conversion rules to transform LaTeX text to Typst markup.

    Args:
        text: The input LaTeX text
        verbose: Whether to print replacement statistics

    Returns:
        The transformed text in Typst format
    """
    for rule in CONVERSION_RULES:
        new_text, n = re.subn(rule.pattern, rule.replacement, text)
        if n and verbose:
            print(f"[{rule.name}] {n} replacements")
        text = new_text
    return text


def print_rules():
    """Print all available conversion rules with their descriptions."""
    print("Available LaTeX to Typst conversion rules:")
    print("=" * 50)
    for rule in CONVERSION_RULES:
        print(f"{rule.name}: {rule.description}")


def process_file(file_path: Path, args) -> None:
    """
    Process a single file with the given arguments.

    Args:
        file_path: Path to the file to process
        args: Parsed command line arguments
    """
    print(f"Processing: {file_path}")
    try:
        data = file_path.read_text(encoding="utf-8")
        transformed = transform(data, verbose=not args.quiet)

        if args.inplace and not args.prefix and not args.suffix:
            file_path.write_text(transformed, encoding="utf-8")
            print(f"Updated in-place: {file_path}")
        else:
            output_name = f"{args.prefix}{file_path.stem}{args.suffix}{args.ext}"
            output_path = file_path.parent / output_name
            output_path.write_text(transformed, encoding="utf-8")
            print(f"Created: {output_path}")

    except UnicodeDecodeError:
        print(f"Warning: Could not decode {file_path} as UTF-8, skipping")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def main():
    """Main entry point for the LaTeX to Typst converter."""
    parser = argparse.ArgumentParser(
        description="Convert LaTeX documents to Typst markup format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s document.tex                    # Convert single file in-place
  %(prog)s --prefix converted_ doc.tex     # Create converted_doc.typ
  %(prog)s --recursive --suffix _typst .  # Convert all .tex files in current dir
  %(prog)s --list-rules                   # Show all conversion rules
        """,
    )

    parser.add_argument("path", nargs="?", help="Path to input file or directory")
    parser.add_argument(
        "--inplace",
        action="store_true",
        help="Replace content in-place (default if no prefix/suffix specified)",
    )
    parser.add_argument(
        "--prefix", type=str, default="", help="Prefix for output files"
    )
    parser.add_argument(
        "--suffix",
        type=str,
        default="",
        help="Suffix for output files (before extension)",
    )
    parser.add_argument(
        "--ext",
        type=str,
        default=".typ",
        help="Extension for output files (default: .typ)",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Process all .tex files under given directory recursively",
    )
    parser.add_argument(
        "--quiet", action="store_true", help="Suppress replacement statistics output"
    )
    parser.add_argument(
        "--list-rules",
        action="store_true",
        help="List all available conversion rules and exit",
    )

    args = parser.parse_args()

    if args.list_rules:
        print_rules()
        return

    if not args.path:
        parser.error("Path argument is required unless using --list-rules")

    path = Path(args.path)

    if not path.exists():
        print(f"Error: Path '{args.path}' does not exist.")
        return 1

    if path.is_file():
        if not path.suffix.lower() == ".tex":
            print(f"Warning: '{path}' does not have .tex extension")
        process_file(path, args)
    elif path.is_dir():
        pattern = "**/*.tex" if args.recursive else "*.tex"
        tex_files = list(path.glob(pattern))

        if not tex_files:
            print(
                f"No .tex files found in {path}"
                + (" (recursive)" if args.recursive else "")
            )
            return 1

        print(f"Found {len(tex_files)} .tex file(s) to process")
        for tex_file in tex_files:
            process_file(tex_file, args)
    else:
        print(f"Error: '{args.path}' is neither a file nor a directory.")
        return 1

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
