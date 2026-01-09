import os
import streamlit as st
from openai import OpenAI

def ai_summarize_text(text: str) -> str:
    if not text or len(text.strip()) == 0:
        return "No text provided to summarize."

    try:
        api_key = os.environ.get("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")
        if not api_key:
            return "Missing OPENAI_API_KEY."

        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Summarize the user's notes clearly and concisely. Max 300 characters."
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            temperature=0.3,
            max_tokens=120,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error generating summary: {e}"

