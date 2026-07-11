from groq import Groq
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def explain_email(email, prediction, confidence):

    prompt = f"""
You are an AI Cybersecurity Assistant.

Email:
{email}

Prediction:
{prediction}

Confidence:
{confidence:.2f}%

Explain in simple English:

1. Why this email is classified this way.
2. Mention suspicious words if any.
3. Give safety advice.
4. Keep answer short (max 150 words).
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],

        temperature=0.3

    )

    return response.choices[0].message.content