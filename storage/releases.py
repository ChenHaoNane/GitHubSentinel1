import os
import json

RELEASE_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "releases")
os.makedirs(RELEASE_DIR, exist_ok=True)

def _repo_to_filename(repo):
    return repo.replace("/", "_") + ".json"

def save_releases(repo, releases):
    filepath = os.path.join(RELEASE_DIR, _repo_to_filename(repo))
    with open(filepath, "w") as f:
        json.dump(releases, f, indent=2)

def load_releases(repo):
    filepath = os.path.join(RELEASE_DIR, _repo_to_filename(repo))
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return json.load(f)
