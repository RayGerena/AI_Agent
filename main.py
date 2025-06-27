import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

if len(sys.argv) > 1:
  prompt = sys.argv[1]
else:
  print("Usage: python3 main.py <prompt>")
  sys.exit(1)

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

print(response.text)

x = response.usage_metadata.prompt_token_count
y = response.usage_metadata.candidates_token_count

print(f"Prompt tokens: {x}\nResponse tokens: {y}")