import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY") or os.environ["GROQ_API_KEY"])


def predict_funding_probability(idea, analysis):

    prompt = f"""
You are a venture capitalist evaluating startup investment opportunities.

Estimate the probability that this startup could raise venture capital funding.

Consider:
- Market size
- Competition
- Scalability
- Business model
- Customer demand
- Innovation

Startup Idea:
{idea}

Startup Analysis:
Industry: {analysis["industry"]}
Target Customers: {analysis["target_customers"]}
Business Model: {analysis["business_model"]}
Market Potential: {analysis["market_potential"]}
Competition Level: {analysis["competition_level"]}

Return ONLY JSON in this format:

{{
 "funding_probability": <number between 0 and 100>
}}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "Respond ONLY with valid JSON."},
            {"role": "user", "content": prompt}
        ]
    )

    result = json.loads(response.choices[0].message.content)

    return result["funding_probability"]
