from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def generate_investor_verdict(idea, analysis, score):

    prompt = f"""
    You are a venture capitalist evaluating startup ideas.

    Startup idea:
    {idea}

    Analysis:
    Industry: {analysis['industry']}
    Target Customers: {analysis['target_customers']}
    Business Model: {analysis['business_model']}
    Market Potential: {analysis['market_potential']}
    Competition Level: {analysis['competition_level']}

    Startup Score: {score}/10

    Write a short investor verdict explaining:
    - strengths
    - risks
    - whether this startup is investable
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content