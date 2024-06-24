# -*- coding: utf-8 -*-
"""Untitled42.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RjY9qE4jnkkAl3lJhgKj4iuS6wDXv9mY
"""

!pip install googletrans==4.0.0-rc1
from googletrans import Translator
def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text
while True:
  if __name__ == "__main__":
    text = input("Enter the text to translate: ")
    src_lang = input("Enter the source language code (e.g., 'en' for English): ")
    dest_lang = input("Enter the destination language code (e.g., 'es' for Spanish): ")
    translated_text = translate_text(text, src_lang, dest_lang)
    print(f"Original text: {text}")
    print(f"Translated text: {translated_text}")