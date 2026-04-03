#!/usr/bin/env python3
"""
Fix ASCII art formatting in BUCH_CLAW_CODE_ARCHITEKTUR.md

Finds all ASCII art blocks that are NOT already inside ``` fenced code blocks
and wraps them in ```text fences so they render correctly in EPUB.

ASCII art detection:
  - Lines starting with +== or +-- (box borders)
  - Lines with box-drawing characters (┌┐└┘├┤─│ etc.)
  - Lines containing flow arrows (-->, ->, ▼, ▲)
  - Lines starting with | ... | that are NOT markdown tables
  - Lines with leading whitespace followed by +-- or | (indented boxes)

Markdown tables (header row + |---| separator + data rows) are NOT modified.

Existing code blocks are validated for proper open/close pairing.
"""

import re
import sys
from pathlib import Path

FILE = Path(__file__).parent / "BUCH_CLAW_CODE_ARCHITEKTUR.md"


def is_markdown_table_line(line: str) -> bool:
    """Return True if the line looks like a standard markdown table row."""
    s = line.strip()
    if not s.startswith("|") or not s.endswith("|"):
        return False
    # Markdown separator row: |---|---|
    if re.match(r"^\|[\s\-:|]+\|$", s):
        return True
    # Markdown data row: | col1 | col2 |  (no box-drawing chars)
    # These typically have multiple pipe-separated cells with text content
    cells = s.split("|")
    # A markdown table row has at least 3 pipes -> 4+ parts after split
    if len(cells) >= 3:
        # Check it doesn't contain box-drawing patterns
        # Note: + can appear in table content (e.g. "100+"), so only flag it
        # if + is adjacent to - or = (box border pattern like +---)
        has_box_drawing = any(ch in s for ch in "┌┐└┘├┤┬┴─│╔╗╚╝║═")
        has_box_border = bool(re.search(r"\+[-=]{2,}", s))
        if not has_box_drawing and not has_box_border:
            return True
    return False


def is_ascii_art_line(line: str) -> bool:
    """Return True if the line is ASCII art (not a markdown table)."""
    stripped = line.rstrip()
    if not stripped:
        return False  # blank lines handled separately

    s = line.lstrip()

    # Box-drawing Unicode characters
    if re.match(r"^[┌┐└┘├┤┬┴─│╔╗╚╝║═╭╮╰╯]", s):
        return True

    # Lines starting with + followed by = or - (box borders)
    if re.match(r"^\+[=\-]{2,}", s):
        return True
    # Indented box borders
    if re.match(r"^\s+\+[=\-]{2,}", line) and not line.startswith("    ") == False:
        if re.match(r"^\s+\+[=\-]{2,}", line):
            return True

    # Lines with flow arrows
    if ("▼" in stripped or "▲" in stripped or "►" in stripped or "◄" in stripped):
        return True

    # Lines that are clearly box content: | ... | with box-drawing or + chars inside
    if s.startswith("|") and s.rstrip().endswith("|"):
        inner = s[1:-1]
        # If it contains +--- or box-drawing chars, it's ASCII art
        if "+--" in inner or any(ch in inner for ch in "┌┐└┘├┤┬┴─│╔╗╚╝║═"):
            return True
        # If it's a wide box line (lots of spaces, typical of diagrams)
        if re.match(r"^\|\s{10,}", s):
            return True

    # Lines that are purely structural: only |, spaces, dashes, equals, plus
    if re.match(r"^[\s|+\-=]+$", stripped) and ("|" in stripped or "+" in stripped) and len(stripped) > 5:
        if "+" in stripped and "-" in stripped:
            return True

    # Lines starting with | containing --> or similar arrows (sequence diagrams)
    if s.startswith("|") and ("-->" in s or "<--" in s or "---" in s):
        return True

    # Indented lines with box-drawing patterns (part of indented diagrams)
    if re.match(r"^\s+[┌┐└┘├┤┬┴─│╔╗╚╝║═╭╮╰╯]", line):
        return True
    if re.match(r"^\s+\+[=\-]{2,}", line):
        return True
    if re.match(r"^\s+\|", line) and ("-->" in line or "<--" in line or "+--" in line):
        return True

    # Lines that look like tree/flow connectors
    if re.match(r"^\s+[\\/|]\s*$", line):
        return True
    if re.match(r"^\s+v\s*$", line):
        return True

    # Sequence diagram headers (Name1  Name2  Name3 with lots of spacing)
    # These are tricky - skip for now

    return False


def is_blank_or_ascii_continuation(line: str) -> bool:
    """Return True if the line is blank (potential continuation between ASCII art blocks)."""
    return line.strip() == ""


def detect_and_wrap(lines: list[str]) -> list[str]:
    """
    Process lines, detect ASCII art outside code blocks, wrap in ```text fences.
    """
    result = []
    i = 0
    n = len(lines)
    in_code_block = False

    while i < n:
        line = lines[i]
        stripped = line.rstrip()

        # Track code block state
        if stripped.startswith("```"):
            if not in_code_block:
                in_code_block = True
            else:
                in_code_block = False
            result.append(line)
            i += 1
            continue

        # If inside a code block, pass through
        if in_code_block:
            result.append(line)
            i += 1
            continue

        # If this is a markdown table line, pass through
        if is_markdown_table_line(line):
            result.append(line)
            i += 1
            continue

        # Check if this line is ASCII art
        if is_ascii_art_line(line):
            # Collect the full ASCII art block
            block_start = i
            block_lines = [line]
            i += 1

            while i < n:
                next_line = lines[i]
                next_stripped = next_line.rstrip()

                # Stop if we hit a code fence
                if next_stripped.startswith("```"):
                    break

                # If next line is ASCII art, include it
                if is_ascii_art_line(next_line):
                    block_lines.append(next_line)
                    i += 1
                    continue

                # If next line is blank, peek ahead to see if ASCII art continues
                if next_line.strip() == "":
                    # Look ahead for more ASCII art (allow up to 2 blank lines)
                    peek = i + 1
                    blank_count = 1
                    while peek < n and lines[peek].strip() == "" and blank_count < 3:
                        peek += 1
                        blank_count += 1

                    if peek < n and is_ascii_art_line(lines[peek]) and not lines[peek].rstrip().startswith("```"):
                        # Include the blank lines and continue
                        for j in range(i, peek):
                            block_lines.append(lines[j])
                        i = peek
                        continue
                    else:
                        break
                else:
                    # Non-ASCII, non-blank line - check if it's a continuation
                    # (e.g., labels in a diagram)
                    # For safety, stop here
                    break

            # Wrap the block
            result.append("```text\n")
            for bl in block_lines:
                result.append(bl)
            # Ensure the block ends with a newline before closing fence
            if block_lines and not block_lines[-1].endswith("\n"):
                result.append("\n")
            result.append("```\n")
        else:
            result.append(line)
            i += 1

    return result


def validate_code_blocks(lines: list[str]) -> list[str]:
    """Check that all code blocks are properly opened and closed."""
    issues = []
    in_code_block = False
    open_line = None

    for i, line in enumerate(lines, 1):
        stripped = line.rstrip()
        if stripped.startswith("```"):
            if not in_code_block:
                in_code_block = True
                open_line = i
            else:
                in_code_block = False
                open_line = None

    if in_code_block:
        issues.append(f"Unclosed code block starting at line {open_line}")

    return issues


def main():
    print(f"Reading {FILE} ...")
    text = FILE.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    total_lines = len(lines)

    # Step 1: Validate existing code blocks
    print("Validating existing code block pairing ...")
    issues = validate_code_blocks(lines)
    if issues:
        for issue in issues:
            print(f"  WARNING: {issue}")
    else:
        print("  All existing code blocks are properly paired.")

    # Step 2: Count ASCII art lines outside code blocks before fix
    in_code = False
    ascii_outside_before = 0
    for line in lines:
        if line.rstrip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code and not is_markdown_table_line(line) and is_ascii_art_line(line):
            ascii_outside_before += 1

    print(f"  Found {ascii_outside_before} ASCII art lines outside code blocks.")

    if ascii_outside_before == 0:
        print("  No ASCII art lines need wrapping. File is already correctly formatted.")
        # Still write the file back (no changes) and verify
        FILE.write_text(text, encoding="utf-8")
        print(f"  File written back ({total_lines} lines, unchanged).")
    else:
        # Step 3: Wrap ASCII art blocks
        print("Wrapping ASCII art blocks in ```text fences ...")
        new_lines = detect_and_wrap(lines)

        # Step 4: Validate result
        result_issues = validate_code_blocks(new_lines)
        if result_issues:
            for issue in result_issues:
                print(f"  ERROR in result: {issue}")
            print("  Aborting: the transformation introduced code block issues.")
            sys.exit(1)

        # Count ASCII art lines outside code blocks after fix
        in_code = False
        ascii_outside_after = 0
        for line in new_lines:
            if line.rstrip().startswith("```"):
                in_code = not in_code
                continue
            if not in_code and not is_markdown_table_line(line) and is_ascii_art_line(line):
                ascii_outside_after += 1

        print(f"  ASCII art lines still outside code blocks after fix: {ascii_outside_after}")

        # Write result
        new_text = "".join(new_lines)
        FILE.write_text(new_text, encoding="utf-8")
        print(f"  File written ({len(new_lines)} lines, was {total_lines}).")

    # Step 5: Final verification
    print("\nFinal verification ...")
    final_text = FILE.read_text(encoding="utf-8")
    final_lines = final_text.splitlines(keepends=True)

    in_code = False
    pipe_outside = []
    for i, line in enumerate(final_lines, 1):
        if line.rstrip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            s = line.strip()
            if s.startswith("|") and s.endswith("|") and len(s) > 3:
                if not is_markdown_table_line(line):
                    pipe_outside.append((i, line.rstrip()))

    if pipe_outside:
        print(f"  WARNING: {len(pipe_outside)} pipe-bounded lines outside code blocks (non-table):")
        for ln, text in pipe_outside[:10]:
            print(f"    Line {ln}: {text[:80]}")
    else:
        print("  OK: All |..| lines outside code blocks are valid markdown tables.")

    # Check code block pairing one more time
    final_issues = validate_code_blocks(final_lines)
    if final_issues:
        for issue in final_issues:
            print(f"  ERROR: {issue}")
    else:
        print("  OK: All code blocks are properly paired (matching open/close).")

    print("\nDone.")


if __name__ == "__main__":
    main()
