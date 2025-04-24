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

# Changelog

## [v0.11] - 2025-04-24

### Added
- Notifier module with support for console output (placeholders for email, wechat, slack)
- Config file `config.json` to manage update intervals and notification methods
- Integrated notifier into scheduler for post-update report delivery

### Changed
- Refactored update logic to improve modularity and future extensibility

---