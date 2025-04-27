# llm/openai_client.py

import os
from openai import OpenAI

# 初始化 OpenAI key
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")

client = OpenAI()
def chat_with_openai(prompt, model="gpt-4o"):
    """用 OpenAI 模型完成一个简单的对话"""
    print(model)
    try:
        response = client.chat.completions.create(
            model = model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        content = response['choices'][0]['message']['content'].strip()
        return content
    except Exception as e:
        raise RuntimeError(f"调用 OpenAI 失败: {e}")
