def render_reports(projects: list[dict]) -> str:
    """Render a list of GitHub project data into a markdown-formatted report string."""
    output = []

    for project in projects:
        info = project.get("info", {})
        releases = project.get("releases", [])
        output.append(f"### {info.get('full_name')}")
        output.append(f"**Description**: {info.get('description', 'N/A')}")
        output.append(f"**Stars**: {info.get('stars', 0)}")
        output.append(f"**Forks**: {info.get('forks', 0)}")
        output.append(f"**Language**: {info.get('language', 'N/A')}")
        output.append(f"**Last Updated**: {info.get('updated_at', 'N/A')}")
        output.append(f"[View on GitHub]({info.get('url')})\n")

        if releases:
            output.append("#### Latest Releases")
            for r in releases:
                output.append(f"- **{r.get('tag_name')}**: {r.get('name', '')}")
                output.append(f"  - Published: {r.get('published_at', '')}")
                body = r.get("body", "").strip()
                if body:
                    body = body[:300] + "..." if len(body) > 300 else body
                    output.append(f"  - {body}")
        else:
            output.append("_No releases found._")

        output.append("\n---\n")

    return "\n".join(output)
