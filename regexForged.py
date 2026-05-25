#!/usr/bin/env python3
import os
import re
import argparse

def main():
    parser = argparse.ArgumentParser(description="In-place batch regex replacement for text files.")
    parser.add_argument("pattern", help="The regex pattern to search for")
    parser.add_argument("replacement", help="The string to replace the pattern with")
    # Added an optional --ext flag that defaults to .md
    parser.add_argument("--ext", default=".md", help="File extension to target (default: .md)")
    args = parser.parse_args()

    try:
        compiled_regex = re.compile(args.pattern)
    except re.error as e:
        print(f"Error: Invalid regex pattern '{args.pattern}' -> {e}")
        return

    files_processed = 0
    total_replacements = 0
    print(f"Scanning local sub-folders for {args.ext} files...")

    for root, _, files in os.walk("."):
        for file in files:
            # Dynamically checks for whatever extension you specify
            if file.lower().endswith(args.ext.lower()):
                file_path = os.path.join(root, file)
                
                content = None
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                except UnicodeDecodeError:
                    try:
                        with open(file_path, "r", encoding="windows-1252") as f:
                            content = f.read()
                    except Exception as e:
                        print(f"Skipped {file_path} due to encoding error: {e}")
                        continue
                except Exception as e:
                    print(f"Skipped {file_path} due to read error: {e}")
                    continue

                if content is None:
                    continue

                try:
                    new_content, count = compiled_regex.subn(args.replacement, content)
                    
                    if count > 0:
                        total_replacements += count
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(new_content)
                    
                    files_processed += 1
                except Exception as e:
                    print(f"Skipped {file_path} during replacement/write: {e}")

    print(f"Done! Processed {files_processed} files. Total replacements made: {total_replacements}")

if __name__ == "__main__":
    main()