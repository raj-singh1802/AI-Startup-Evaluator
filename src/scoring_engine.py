import os
import re
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY") or os.environ["GROQ_API_KEY"])


def score_startup(idea, analysis):

    prompt = f"""
You are a senior venture capitalist evaluating startup ideas.

Score this startup from 0 to 10.

Evaluation criteria:

1. Market Opportunity
2. Competitive Advantage
3. Business Model Strength
4. Customer Demand
5. Innovation / Differentiation

Scoring guide:

9-10 = Exceptional startup with strong potential  
7-8 = Strong opportunity  
5-6 = Average but viable  
3-4 = Weak opportunity  
0-2 = Very poor idea

Startup Idea:
{idea}

Startup Analysis:
Industry: {analysis['industry']}
Target Customers: {analysis['target_customers']}
Business Model: {analysis['business_model']}
Market Potential: {analysis['market_potential']}
Competition Level: {analysis['competition_level']}

Return ONLY JSON in this format:

{{
  "score": <number between 0 and 10>,
  "breakdown": {{
    "market": <number between 0 and 10>,
    "competition": <number between 0 and 10>,
    "business_model": <number between 0 and 10>,
    "demand": <number between 0 and 10>,
    "innovation": <number between 0 and 10>
  }}
}}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "Respond ONLY with valid JSON."},
            {"role": "user", "content": prompt}
        ]
    )

    result_text = response.choices[0].message.content.strip()

    try:
        json_match = re.search(r'\{.*\}', result_text, re.DOTALL)

        if json_match:
            result = json.loads(json_match.group())
        else:
            result = json.loads(result_text)

        score = float(result.get("score", 5))

        return result

    except Exception:
        return {
            "score": 5.0,
            "breakdown": {
                "market": 5.0,
                "competition": 5.0,
                "business_model": 5.0,
                "demand": 5.0,
                "innovation": 5.0
            }
        }


def startup_recommendation(idea, score, funding_probability):

    prompt = f"""
You are a venture capitalist giving investment advice.

Startup Idea:
{idea}

Startup Score: {score}/10
Funding Probability: {funding_probability}%

Write a concise recommendation explaining whether this startup is:

• A strong investment opportunity
• Promising but needs differentiation
• A risky idea

Explain briefly why.

Return ONLY the recommendation text.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
