# Changelog

All notable changes to this project will be documented in this file.

## [v0.1] - 2025-04-23

### Added
- Initial CLI tool with `track`, `list`, `remove`, `update`, `releases`, `help`, and `quit` commands
- GitHub API integration to fetch repository information
- Local storage in JSON format to save tracked repositories and release notes
- Simple and clean output formatting using `click` library
- `.gitignore`, `README.md`, `Makefile`, and basic project structure
- Command-line interface that runs in an interactive mode

### Fixed
- Default fallback for `track` command when no repository argument is provided

---

## Upcoming versions
- v0.2: GitHub OAuth support, Background task scheduler, Database storage integration
