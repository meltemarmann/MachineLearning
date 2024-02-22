import pathlib
import textwrap

import google.generativeai as genai

# Used to securely store your API key
import os

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY='AIzaSyATK-TatU6Xs7Egg3jiE4xGYMXJ2I4Fd4s'
genai.configure(api_key=GOOGLE_API_KEY)

"""for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)"""
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("What is the meaning of life?")
print(to_markdown(response.text).data)
print(response.prompt_feedback)
print(response.prompt_feedback.type)