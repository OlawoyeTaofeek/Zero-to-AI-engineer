import os
from dotenv import load_dotenv
from openai import OpenAI
from typing import List, Dict, Optional

load_dotenv()

class OpenAIAPI:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        self.client = OpenAI(api_key=self.api_key)
        self.default_model = "gpt-4o"  # gpt-5 doesn't exist yet

    def generate_response(
        self,
        messages: List[Dict],
        system_prompt: str,
        model: Optional[str] = None,
        max_tokens: Optional[int] = None,
        temperature: float = 0.3
    ):
        try:
            # OpenAI takes system prompt as a message, not a separate parameter
            full_messages = [{"role": "system", "content": system_prompt}] + messages

            response = self.client.chat.completions.create(
                model=model or self.default_model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=full_messages
            )

            # OpenAI response shape is different from Anthropic
            reply = response.choices[0].message.content
            usage = response.usage
            return usage, reply

        except Exception as e:
            return "error", str(e)

    def generate_response_stream(
        self,
        messages: List[Dict],
        system_prompt: str,
        model: Optional[str] = None,
        max_tokens: Optional[int] = None,
        temperature: float = 0.3
    ):
        try:
            full_messages = [{"role": "system", "content": system_prompt}] + messages

            stream = self.client.chat.completions.create(
                model=model or self.default_model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=full_messages,
                stream=True,
                stream_options={"include_usage": True}  # needed to get usage in stream
            )
            return stream

        except Exception as e:
            return "error", str(e)