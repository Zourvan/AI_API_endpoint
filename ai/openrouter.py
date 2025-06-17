import os
import requests
import json
from .base import AIPlatform


class OpenRouter(AIPlatform):
    def __init__(self, api_key: str, system_prompt: str = None):
        self.api_key = api_key
        self.system_prompt = system_prompt
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://your-app-url.com",  # Replace with your actual site URL
            "X-Title": "AI API Service",  # Replace with your actual site name
        }
        self.model = (
            "deepseek/deepseek-r1-0528-qwen3-8b:free"  # Default model, can be changed
        )

    def chat(self, prompt: str) -> str:
        messages = []

        # Add system prompt if available
        if self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})

        # Add user message
        messages.append({"role": "user", "content": prompt})

        payload = {"model": self.model, "messages": messages}

        try:
            response = requests.post(
                url=self.base_url, headers=self.headers, data=json.dumps(payload)
            )

            response.raise_for_status()  # Raise exception for HTTP errors
            result = response.json()

            if "choices" in result and len(result["choices"]) > 0:
                return result["choices"][0]["message"]["content"]
            else:
                return "No response generated."

        except requests.exceptions.RequestException as e:
            raise Exception(f"OpenRouter API error: {str(e)}")
