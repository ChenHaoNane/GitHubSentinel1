import textwrap

def print_formatted_releases(releases):
    if not releases:
        print("🔍 暂无 release 信息。")
        return

    print("\n📦 最近的 Releases：\n")

    for rel in releases:
        tag = rel.get("tag_name", "N/A")
        name = rel.get("name", "No title")
        published = rel.get("published_at", "Unknown date")
        body = rel.get("body", "")

        print(f"🔸 {tag} — {name} ({published})")
        print(textwrap.indent(textwrap.fill(body, width=80), prefix="    "))
        print("-" * 80)
