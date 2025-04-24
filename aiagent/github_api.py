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
