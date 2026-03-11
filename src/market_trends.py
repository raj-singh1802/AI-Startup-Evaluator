import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def analyze_market_trend(idea, analysis):

    prompt = f"""
    You are a venture capital market analyst.

    Analyze the market trends for the following startup idea.

    Startup idea:
    {idea}

    Industry:
    {analysis["industry"]}

    Explain:
    - current market demand
    - growth potential
    - risks or saturation

    Keep the answer concise (4–5 sentences).
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content