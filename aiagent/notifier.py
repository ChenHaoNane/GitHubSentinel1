def notify(report: str, method: str = "console"):
    """
    Notify the user with the rendered report using the selected method.
    :param report: Rendered report string
    :param method: Notification method (console, email, wechat, slack)
    """
    if method == "console":
        print("\n📢 Notification via Console:\n")
        print(report)
    elif method == "email":
        # TODO: Implement email sending
        print("[模拟通知] 发送到 Email")
    elif method == "wechat":
        # TODO: Implement WeChat Work webhook
        print("[模拟通知] 发送到 企业微信")
    elif method == "slack":
        # TODO: Implement Slack webhook
        print("[模拟通知] 发送到 Slack")
    else:
        print(f"⚠️ Unknown notification method: {method}")
