![Apps rePhorged](Apps_rePhorged.png)

# regexPhorge

A high-performance command-line utility designed for fast, in-place batch regular expression replacements across thousands of localized text and Markdown files.

## Overview

When migrating massive datasets or archival documents (such as legacy HTML and game rulesets) into modern structured formatting, standard IDE tools often struggle under the memory and user interface overhead of tracking tens of thousands of simultaneous line modifications. `regexPhorge` solves this bottleneck by providing a headless, ultra-lean execution layer that cuts through thousands of nested sub-folders and files in mere seconds. Operating completely in-place, it pre-compiles search patterns, minimizes unnecessary disk-write actions, and implements resilient encoding fallback mechanisms to seamlessly upgrade legacy character structures into clean, standardized document files.

## Features

- **Blazing Fast In-Place Swaps:** Directly modifies file content natively without any structural overhead or UI rendering delays.
- **Smart Disk-Write Management:** Pre-checks matches using pre-compiled byte regex patterns and completely skips the file system write process if zero replacements are identified.
- **Automated Encoding Resilience:** Attempts primary reading in standard UTF-8 and gracefully falls back to Windows-1252 (CP1252) for legacy formats, ultimately saving files out as clean UTF-8 to resolve encoding mismatches.
- **Dynamic File Targeting:** Built-in deep directory scanning targets custom extensions (such as `.md` or `.htm`) down through infinitely nested folder layouts.
- **Live Output Reporting:** Displays real-time operational feedback, featuring accurate summaries tracking total files successfully modified and total structural replacements completed.

## Requirements

- Python 3.6+
- Built entirely using standard library modules (`os`, `re`, `sys`, `argparse`). No third-party modules are required.

## Installation

**Download** the script to your local machine. You can clone the repository or download the latest release:

```
git clone https://github.com/oldmanumby/regexPhorge.git cd regexPhorge
```

## Configuration

When running `regexPhorge`, parameters are passed explicitly as command-line arguments. The utility processes inputs based on three primary components:

1. **pattern:** The specific regular expression sequence to find within the localized documents.
2. **replacement:** The clean string or layout syntax to substitute in place of the detected target pattern.
3. **--ext:** An optional flag declaring the precise file extension constraint to evaluate (defaults explicitly to `.md`).

No separate configuration files are required, allowing for uninterrupted automation and zero configuration state persistence across bulk project operations.

## Usage

Ensure you wrap your arguments cleanly in single quotes when executing commands inside your terminal shell to prevent the OS from pre-parsing quotes or backslashes before they safely reach Python's regex engine.

### Running the Script

You can execute the script from your terminal or command prompt:

```
python3 regexPhorge.py 'pattern' 'replacement' [--ext .ext]
```

Or using your explicit environment path:

```
/opt/homebrew/bin/python3 regexPhorge.py 'pattern' 'replacement' [--ext .ext]
```

### Example Workflows

1. **Stripping Out Explicit HTML Tags:** Wipe out unneeded paragraph markup elements globally across your Markdown workspace files:

```
python3 regexPhorge.py '<p>' ''
```
   
2. **Formatting Header Structures with Embedded Content:** Convert old-school font style parameters safely into clean Markdown headings while insulating double quotes from terminal shell fragmentation:

```
python3 regexPhorge.py '<FONT SIZE="6">' '## '
```
   
3. **Collapsing Fragmented Multi-Line Newlines:** Scan across multi-line blocks to safely transform duplicate empty vertical margins into a single-blank layout line break:

```
python3 regexPhorge.py '\n{3,}' '\n\n'
```
   
4. **Stitching Broken Sentence Wrap Segments:** Mend premature line-wrap sentence separations while fully insulating your actual double-newline paragraph layouts:


```
python3 regexPhorge.py '(?<=[^\n])\n(?=[^\n])' ' '
```

## Advanced Features

- **Isolated Newline Lookaround Targeting:** Utilizes state-aware positive lookbehind `(?<=[^\n])` and lookahead `(?=[^\n])` bounds to smoothly correct lineation issues inside flowing bodies of text without cross-contaminating block margins.
- **Legacy Bit Upgrades:** Seamlessly catches legacy characters (such as smart quotes or fractions) embedded inside Western European text, sanitizing and re-encoding the destination block as localized UTF-8 text on save.

## Troubleshooting

- **Total Replacements Made Displays 0:** Double-check your outer string quotation strategy. If your pattern incorporates nested double quotes, preserve their inner properties by encapsulating the parameter inside single quotes (`'...'`) in the shell.
- **Skipped File Reading Errors:** If items are marked as skipped due to a file-not-found error, verify that the files are physically available on your local system drive and are not currently offloaded or evicted by active cloud replication filters.

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

You are free to use, modify, and distribute this software, provided that you:

- Disclose the source code of any modifications you make.
- License your modified versions under the same GPL-3.0 license.
- Preserve the original copyright notices and disclaimers.

See the [LICENSE](LICENSE) file for the complete text of the GPL-3.0 license.
