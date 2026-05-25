# [regexPhorge] Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **Dry-Run Flag Optimization:** Ongoing development of a placeholder flag to preview matched string modifications without writing edits immediately to disk.

## [v1.0.0] - 2026-05-25

### Added

- **Initial Core Engine Release:** Deployed standard structural loop featuring headless pre-compiled file scanning using Python's raw `re.subn` layer.
- **Resilient Multi-Encoding Reader Fallback:** Integrated dynamic fallback handling that attempts UTF-8 parsing and safely transitions to Windows-1252 to process legacy documents without breaking pipeline flows.
- **Global Replacement Accumulator Reporting:** Implemented tracking functionality to log and output the total sum of structural alterations performed globally alongside total modified files.
- **Dynamic Command Line Flag Targeting:** Added default support to automatically scan for `.md` target blocks with full multi-extension override configurations via CLI argument inputs.