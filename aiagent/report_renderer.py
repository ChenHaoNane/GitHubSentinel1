def render_reports(repos_data: list) -> str:
    """
    Render report content from repositories data.
    
    :param repos_data: List of dicts with repo, info, releases, pull_requests, issues
    :return: Markdown format string
    """
    if not repos_data:
        return "No data available for reporting."

    report_lines = ["# 📋 Daily Progress Report\n"]

    for repo_data in repos_data:
        repo = repo_data.get("repo")
        info = repo_data.get("info", {})
        releases = repo_data.get("releases", [])
        pull_requests = repo_data.get("pull_requests", [])
        issues = repo_data.get("issues", [])

        report_lines.append(f"## 📌 {repo}")
        report_lines.append(f"- **Description**: {info.get('description', 'N/A')}")
        report_lines.append(f"- **Language**: {info.get('language', 'N/A')}")
        report_lines.append(f"- **Last Updated**: {info.get('updated_at', 'N/A')}")
        report_lines.append(f"- **Stars**: ⭐ {info.get('stars', 'N/A')}")
        report_lines.append("")

        # Releases Section
        if releases:
            report_lines.append("### 🚀 Recent Releases")
            for release in releases:
                report_lines.append(f"- **[{release['tag_name']}] {release['name']}** ({release['published_at']})")
                if release.get('body'):
                    body_snippet = release['body'][:150] + "..." if len(release['body']) > 150 else release['body']
                    report_lines.append(f"  > {body_snippet}")
            report_lines.append("")
        
        # Pull Requests Section
        if pull_requests:
            report_lines.append("### 🔀 Recent Pull Requests")
            for pr in pull_requests:
                report_lines.append(f"- [{pr['title']}]({pr['url']}) by {pr['user']} ({pr['created_at']})")
            report_lines.append("")

        # Issues Section
        if issues:
            report_lines.append("### 🐛 Recent Issues")
            for issue in issues:
                report_lines.append(f"- [{issue['title']}]({issue['url']}) by {issue['user']} ({issue['created_at']})")
            report_lines.append("")

        report_lines.append("---\n")

    return "\n".join(report_lines)
