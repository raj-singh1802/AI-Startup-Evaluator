import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY") or os.environ["GROQ_API_KEY"])


def analyze_startup(idea):

    prompt = f"""
Analyze the following startup idea.

Return ONLY JSON.

IMPORTANT:
market_potential must be one of: High, Medium, Low
competition_level must be one of: High, Medium, Low

Format:

{{
  "industry": "",
  "target_customers": "",
  "business_model": "",
  "market_potential": "High | Medium | Low",
  "competition_level": "High | Medium | Low"
}}

Startup Idea: {idea}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",  # updated to a valid currently supported groq model
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content

    return json.loads(result)

if __name__ == "__main__":
    analysis = analyze_startup("AI mental health chatbot")
    print(json.dumps(analysis, indent=4))