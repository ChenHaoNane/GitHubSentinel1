import os
import requests
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

GITHUB_API = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def _headers():
    """构造请求头，包括可选的授权 token"""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "GitHub-Sentinel-Agent"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


def _check_token():
    """检测 GITHUB_TOKEN 是否存在，并检测其是否有效"""
    if not GITHUB_TOKEN:
        raise EnvironmentError("❌ GITHUB_TOKEN 未设置，请在 .env 文件中添加你的 GitHub token。")

    # 发送一个无害请求来测试 token 是否有效
    resp = requests.get(f"{GITHUB_API}/rate_limit", headers=_headers())
    if resp.status_code == 401:
        raise PermissionError("❌ 无效的 GITHUB_TOKEN，请检查 token 是否正确或已过期。")


def fetch_repo_info(repo):
    _check_token()

    url = f"{GITHUB_API}/repos/{repo}"
    response = requests.get(url, headers=_headers())

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
        raise Exception(f"GitHub API error: {response.status_code} - {response.text}")


def fetch_repo_releases(repo, count=1):
    _check_token()

    url = f"{GITHUB_API}/repos/{repo}/releases"
    resp = requests.get(url, headers=_headers())

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
            "body": (release.get("body")[:300] + "...") if release.get("body") else ""
        })

    return releases
def fetch_pull_requests(repo):
    """
    Fetch open pull requests for a given GitHub repository.
    :param repo: format 'owner/repo'
    :return: list of pull request dicts
    """
    url = f"{GITHUB_API}/repos/{repo}/pulls"
    response = requests.get(url, headers=_headers())

    if response.status_code != 200:
        raise Exception(f"Failed to fetch pull requests for {repo}: {response.status_code} {response.text}")

    return response.json()

def fetch_issues(repo):
    """
    Fetch open issues for a given GitHub repository.
    (excluding pull requests)
    :param repo: format 'owner/repo'
    :return: list of issue dicts
    """
    url = f"{GITHUB_API}/repos/{repo}/issues"
    params = {"state": "open", "filter": "all"}
    response = requests.get(url, headers=_headers(), params=params)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch issues for {repo}: {response.status_code} {response.text}")

    # GitHub API 把 PR 也算进 issues，需要过滤掉
    issues = [issue for issue in response.json() if "pull_request" not in issue]
    return issues

def fetch_repo_all(repo):
    """一次性拉取 repo 的信息、releases、PRs、issues"""
    info = fetch_repo_info(repo)
    releases = fetch_repo_releases(repo)
    pulls = fetch_pull_requests(repo)
    issues = fetch_issues(repo)

    return {
        "repo": repo,
        "info": {
            "full_name": info.get("full_name"),
            "description": info.get("description"),
            "stars": info.get("stargazers_count"),
            "updated_at": info.get("updated_at"),
            "url": info.get("html_url"),
        },
        "releases": releases,
        "pull_requests": pulls,
        "issues": issues
    }

def save_daily_progress(date_str, repo, pull_requests, issues, output_dir="storage/data"):
    """
    Save today's pull requests and issues into a Markdown file.
    :param date_str: 'YYYY-MM-DD'
    :param repo: 'owner/repo'
    :param pull_requests: list of PR dicts
    :param issues: list of issue dicts
    :param output_dir: where to save the markdown file
    """
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"{date_str}.md")
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"# Progress Report for {repo} on {date_str}\n\n")
        
        f.write("## Pull Requests:\n")
        if pull_requests:
            for pr in pull_requests:
                f.write(f"- [{pr['title']}]({pr['html_url']}) by @{pr['user']['login']}\n")
        else:
            f.write("- No open pull requests.\n")

        f.write("\n## Issues:\n")
        if issues:
            for issue in issues:
                f.write(f"- [{issue['title']}]({issue['html_url']}) by @{issue['user']['login']}\n")
        else:
            f.write("- No open issues.\n")
        
        f.write("\n---\n\n")