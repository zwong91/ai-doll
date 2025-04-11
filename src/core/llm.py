import requests

class LLMClient:
    def __init__(self, url="http://localhost:11434/api/generate", model="qwen2.5:0.5b"):
        self.url = url
        self.model = model

    def get_response(self, text):
        """获取AI响应"""
        data = {
            "model": self.model,
            "prompt": text,
            "stream": False
        }
        response = requests.post(self.url, json=data)
        return response.json()["response"]
