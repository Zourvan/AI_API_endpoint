import os
import google.generativeai as genai
from .base import AIPlatform


class Gemini(AIPlatform):
    def __init__(self, api_key: str, system_prompt: str = None):
        self.api_key = api_key
        self.system_prompt = system_prompt
        genai.configure(api_key=self.api_key)

        # Using a more widely available model instead of preview
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    def chat(self, prompt: str) -> str:
        if self.system_prompt:
            prompt = f"{self.system_prompt}\n\n{prompt}"

        response = self.model.generate_content(prompt)
        return response.text
