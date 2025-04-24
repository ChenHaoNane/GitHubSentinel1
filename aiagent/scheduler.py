import os
import json
import click
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from aiagent.github_api import fetch_repo_info, fetch_repo_releases
from aiagent.report_renderer import render_reports
from aiagent.notifier import notify
from storage.local import load_tracked_repos

TRACK_FILE = "tracked_repos.json"

def load_config():
    """从 config.json 文件中加载配置"""
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        raise FileNotFoundError("config.json 文件未找到")
    except json.JSONDecodeError:
        raise ValueError("config.json 格式无效")

def update_projects():
    """定时更新项目列表"""
    click.echo(f"\n[{datetime.now()}] - Running scheduled update task...")

    tracked_repos = load_tracked_repos(TRACK_FILE)
    all_data = []
    if not tracked_repos:
        click.echo("❌ 错误: 没有可追踪的仓库")
        return
    try:
        for repo in tracked_repos:
            repo_info = fetch_repo_info(repo)
            releases = fetch_repo_releases(repo, count=1)  # 获取最新 release 信息
            all_data.append({"repo": repo, "info": repo_info, "releases": releases})
    except Exception as e:
        click.echo(f"❌ 错误: 定时更新失败，原因：{str(e)}")
    report = render_reports(all_data)
    notify(report, method="console")  # ✅ 默认 console，未来可改为 email、wechat、slack

def start_scheduler():
    """启动定时任务调度器"""
    config = load_config()
    update_frequency_seconds = config.get("update_frequency_seconds", 1)
    
    scheduler = BackgroundScheduler()
    # 使用配置的更新频率（单位： 秒）
    scheduler.add_job(update_projects, 'interval', seconds=update_frequency_seconds)
    scheduler.start()
    return scheduler
