import requests

GITHUB_API = "https://api.github.com"

def fetch_repo_info(repo):
    """
    Fetch basic info about a GitHub repository using GitHub REST API.
    :param repo: format 'owner/repo'
    :return: dict containing repository info
    """
    url = f"{GITHUB_API}/repos/{repo}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "full_name": data.get("full_name"),
            "description": data.get("description"),
            "stars": data.get("stargazers_count"),
            "forks": data.get("forks_count"),
            "language": data.get("language"),
            "updated_at": data.get("updated_at"),
            "url": data.get("html_url"),
        }
    elif response.status_code == 404:
        raise ValueError(f"Repository '{repo}' not found.")
    else:
        raise Exception(f"GitHub API error: {response.status_code}")


def fetch_repo_releases(repo, count=1):
    url = f"{GITHUB_API}/repos/{repo}/releases"
    headers = {"Accept": "application/vnd.github+json"}
    resp = requests.get(url, headers=headers)

    if resp.status_code != 200:
        raise Exception(f"获取 release 信息失败: {resp.status_code} {resp.text}")

    data = resp.json()
    if not data:
        return []

    releases = []
    for release in data[:count]:
        releases.append({
            "tag_name": release.get("tag_name"),
            "name": release.get("name"),
            "published_at": release.get("published_at"),
            "body": release.get("body")[:300] + "..." if release.get("body") else ""
        })

    return releases