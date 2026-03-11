import os
import csv
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ["GROQ_API_KEY"])


def generate_startups(batch_size=50):

    prompt = f"""
Generate {batch_size} realistic AI startup companies.

Return ONLY CSV format with two columns:

name,description

Example:

Woebot,AI chatbot for mental health therapy
Harvey AI,AI legal assistant for law firms

Focus on industries like:
AI healthcare
AI finance
AI developer tools
AI marketing
AI education
AI robotics
AI productivity
AI legal tech
AI cybersecurity
AI climate tech
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def main():

    file_path = "data/startups.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow(["name", "description"])

        for i in range(10):  # 10 batches × 50 = 500 startups

            print(f"Generating batch {i+1}...")

            csv_data = generate_startups()

            lines = csv_data.strip().split("\n")

            for line in lines:

                if "," in line:
                    name, desc = line.split(",", 1)
                    writer.writerow([name.strip(), desc.strip()])

    print("Dataset generated successfully!")


if __name__ == "__main__":
    main()