# 🧠 GitHub Sentinel

AI Agent CLI tool for tracking open-source projects on GitHub.  
Fetch stars, release notes, and repository updates — all in one place.  
Perfect for developers, investors, and enthusiasts who want to monitor innovation in real-time.

---

## 🚀 Features

- 📌 **Track** any public GitHub repository
- 🌟 Fetch real-time star counts & description
- 📝 View detailed **release notes**
- 🔄 Update tracked projects automatically
- 💾 Local JSON-based storage (easy to switch to database)
- ⚙️ CLI-based interactive mode with persistent commands

---

## 📦 Installation

### Clone the repo

```bash
git clone https://github.com/ChenHaoNane/GitHubSentinel1.git
cd github-sentinel
```

### Setup Python environment (Python 3.12)

```bash
# Create virtual environment (optional)
python3.12 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🛠️ Usage

### Run the CLI

```bash
python -m aiagent.cli
```

You will enter an interactive mode. Available commands:

```text
track <repo>        - Track a new GitHub repository (e.g., openai/openai-python)
list                - List all tracked repositories
remove <repo>       - Remove a repository from tracking
update              - Fetch latest info for all tracked repos
releases <repo>     - Show release notes for a given repository
help                - Show help message
quit                - Exit the CLI
```

### Example:

```bash
>>> track openai/openai-python
>>> releases openai/openai-python
>>> update
```

---

## 🗂️ Project Structure

```
aiagent/
├── cli.py                  # CLI entry point (Click-based)
├── github_api.py           # GitHub API integration
├── storage/
│   ├── tracked.py          # Track/remove/list/save repos
│   └── releases.py         # Release storage and loading
├── utils/
│   └── format.py           # Output formatting utilities
├── data/
│   └── releases/           # JSON files storing release info
```

---

## 📄 License

MIT License © 2025 Haonan Chen

---

## 🌐 Roadmap

- [ ] SQLite/PostgreSQL storage backend
- [ ] Web UI dashboard
- [ ] GitHub OAuth integration
- [ ] Scheduled background updates
- [ ] Agent-style push alerts (e.g., Discord, Telegram, Slack)

---

## 🤝 Contributing

Pull requests and feedback are welcome!  
Feel free to fork this project and improve it ✨