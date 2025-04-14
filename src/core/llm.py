import requests

class LLMClient:
    def __init__(self, 
                 url: str = "http://localhost:11434/api/generate", 
                 model: str = "qwen2.5:0.5b",
                 num_predict: int = 64):
        self.url = url
        self.model = model
        self.num_predict = num_predict

    def get_response(self, text):
        """获取AI响应"""
        data = {
            "model": self.model,
            "prompt": text,
            "stream": False,
            "options": {
                'num_predict': self.num_predict,
                'temperature': 1,
            },
        }
        response = requests.post(self.url, json=data)
        return response.json()["response"]