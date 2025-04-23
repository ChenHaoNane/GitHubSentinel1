import json
import os

def load_tracked_repos(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r') as f:
        return json.load(f)

def save_tracked_repos(filepath, repos):
    with open(filepath, 'w') as f:
        json.dump(repos, f, indent=2)
