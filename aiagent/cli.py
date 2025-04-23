import shlex
from click.testing import CliRunner
import click
from aiagent.github_api import fetch_repo_info, fetch_repo_releases
from storage.local import load_tracked_repos, save_tracked_repos
from storage.releases import save_releases, load_releases
from utils.format import print_formatted_releases

TRACK_FILE = "tracked_repos.json"

def print_dynamic_welcome():
    click.echo("🎯 AI Agent CLI — 请输入命令（输入 quit 退出）\n")
    click.echo("可用命令：")
    for name, command in cli.commands.items():
        help_text = command.get_short_help_str()
        click.echo(f"  🔹 {name:<20} - {help_text}")
    click.echo("")

@click.group()
def cli():
    """AI Agent CLI - Track GitHub open-source projects"""
    click.echo("\n🚀 Welcome to the AI Agent CLI!")
    click.echo("Type 'quit' to exit or 'help' to see available commands.\n")
    click.echo("Available commands:")
    click.echo(" - track <repo>:     Track a new GitHub repository")
    click.echo(" - list:             List tracked repositories")
    click.echo(" - remove <repo>:    Remove a tracked repository")
    click.echo(" - update:           Update all tracked repositories")
    click.echo(" - releases <repo>:  View the release notes for a repository\n")

@cli.command()
def help():
    """显示所有可用命令及其说明"""
    click.echo("\n🆘 帮助信息：可用命令如下：\n")
    click.echo(" - track <repo>     📌 追踪一个新的 GitHub 仓库")
    click.echo(" - list             📂 显示所有被追踪的仓库")
    click.echo(" - remove <repo>    ❌ 移除一个被追踪的仓库")
    click.echo(" - update           🔄 更新所有仓库信息")
    click.echo(" - releases <repo>  📝 查看指定仓库的 release notes")
    click.echo(" - help             🆘 显示此帮助信息")
    click.echo(" - quit             👋 退出 CLI\n")
    
@cli.command()
@click.argument('repo', default='openai/gpt-4')
def track(repo):
    """Track a new GitHub repo"""
    repos = load_tracked_repos(TRACK_FILE)
    if repo in repos:
        click.echo(f"{repo} is already tracked.")
    else:
        try:
            info = fetch_repo_info(repo)
            click.echo(f"Tracking {repo}...")
            click.echo(f"- Name: {info['full_name']}")
            click.echo(f"- Description: {info['description']}")
            click.echo(f"- Stars: {info['stars']}")
            click.echo(f"- Updated At: {info['updated_at']}")
            repos.append(repo)
            save_tracked_repos(TRACK_FILE, repos)
        except Exception as e:
            click.echo(f"Error: {str(e)}")

@cli.command()
def list():
    """List tracked repositories"""
    repos = load_tracked_repos(TRACK_FILE)
    if repos:
        click.echo("Tracked repositories:")
        for r in repos:
            click.echo(f"- {r}")
    else:
        click.echo("No repositories tracked.")

@cli.command()
@click.argument('repo', default='openai/gpt-4')  # 默认 repo 参数
def remove(repo):
    """Remove a tracked repository"""
    repos = load_tracked_repos(TRACK_FILE)
    if repo in repos:
        repos.remove(repo)
        save_tracked_repos(TRACK_FILE, repos)
        click.echo(f"Removed {repo}.")
    else:
        click.echo(f"{repo} is not being tracked.")

@cli.command()
def update():
    """Simulate update of tracked repositories"""
    repos = load_tracked_repos(TRACK_FILE)
    if not repos:
        click.echo("No repositories to update.")
    else:
        click.echo("Updating tracked repositories:")

        for repo in repos:
            click.echo(f"- Checking {repo}...")
            releases = fetch_repo_releases(repo)
            if releases:
                save_releases(repo, releases)
                click.echo("\n📦 最近的 Releases：")
                for rel in releases:
                    click.echo(f"- [{rel['tag_name']}] {rel['name']} ({rel['published_at']})")
                    click.echo(f"  {rel['body']}\n")
            else:
                click.echo("🔍 暂无 release 信息。")

@cli.command()
@click.argument("repo")
def releases(repo):
    """查看仓库的 Release Notes"""
    click.echo(f"📖 正在加载 {repo} 的 Release Notes...")
    try:
        releases = load_releases(repo)
        print_formatted_releases(releases)
    except Exception as e:
        click.echo(f"❌ 加载失败: {str(e)}")

@cli.command()
def quit():
    """Quit the AI Agent CLI"""
    click.echo("Goodbye!")
    raise SystemExit

if __name__ == "__main__":
    runner = CliRunner()
    print_dynamic_welcome()

    click.echo("🎯 AI Agent CLI — Type a command or `quit` to exit.")
    while True:
        try:
            cmd = input(">>> ").strip()
            if not cmd:
                continue
            if cmd.lower() in {"exit", "quit"}:
                click.echo("👋 Goodbye!")
                break
            result = runner.invoke(cli, shlex.split(cmd))
            if result.output:
                click.echo(result.output.strip())
            if result.exception:
                raise result.exception
        except (KeyboardInterrupt, EOFError):
            click.echo("\n👋 Exiting.")
            break
        except Exception as e:
            click.echo(f"❌ Error: {e}")
