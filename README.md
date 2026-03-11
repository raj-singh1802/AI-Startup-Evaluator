🚀 AI Startup Evaluator

An AI-powered platform that evaluates startup ideas using Large Language Models, vector similarity search, and a scoring engine to simulate how venture capital firms assess startups.

The system analyzes an idea, predicts its funding potential, compares it with similar startups, and generates an investor-style evaluation report.

📸 Dashboard Preview
Startup Evaluation Dashboard
<img width="1836" height="955" alt="dashboard" src="https://github.com/user-attachments/assets/9be62a8f-e1f6-41f7-88db-1dc938948e7c" />

Startup Analysis
<img width="1343" height="915" alt="startup-analysis" src="https://github.com/user-attachments/assets/97cd4b73-4c20-4c71-81a2-0b4c91bf7c0e" />

Startup Score
<img width="1375" height="893" alt="startup-score" src="https://github.com/user-attachments/assets/a4ae3d97-4169-4271-a737-c352e127d40f" />

Startup Metrics Radar Chart
<img width="639" height="558" alt="startup-metrics-overview" src="https://github.com/user-attachments/assets/14b2b722-6dd9-4928-95cf-de72d11a55e2" />

🔹 Features
🤖 AI Startup Idea Analysis

Uses an LLM to analyze startup ideas and extract:

Industry

Target customers

Business model

Market potential

Competition level

📊 Startup Scoring Engine

A scoring system that evaluates:

Market potential

Competitive advantage

Innovation

Risk level

💰 Funding Probability Predictor

Estimates the probability of venture capital funding based on the startup characteristics.

🔎 Similar Startup Detection

Uses:

Sentence Transformers

FAISS Vector Search

to find real similar startups from the dataset.

🧠 AI VC Investor Verdict

Generates a venture capitalist style investment opinion explaining:

strengths

risks

investment viability

📈 Market Trend Analysis

Analyzes the industry trends and growth potential for the startup idea.

📊 Interactive Dashboard

Built with Streamlit, featuring:

Score gauge visualization

Radar analytics chart

Similar startup insights

Downloadable evaluation report

🧠 Tech Stack
Category	Technology
Language	Python
UI Framework	Streamlit
LLM API	Groq
Embeddings	Sentence Transformers
Vector Search	FAISS
Visualization	Plotly
Data	CSV Dataset
📊 System Architecture
User Startup Idea
        │
        ▼
LLM Startup Analyzer
        │
        ▼
Startup Scoring Engine
        │
        ▼
Funding Probability Predictor
        │
        ▼
Vector Similarity Search (FAISS)
        │
        ▼
AI VC Investor Verdict
        │
        ▼
Market Trend Analyzer
        │
        ▼
Interactive Streamlit Dashboard
📂 Project Structure
AI-Startup-Evaluator
│
├── api
│   └── main.py
│
├── app
│   └── streamlit_app.py
│
├── assets
│   ├── dashboard.png
│   ├── startup-analysis.png
│   ├── startup-score.png
│   └── startup-metrics-overview.png
│
├── data
│   └── startups.csv
│
├── scripts
│   └── generate_startup_dataset.py
│
├── src
│   ├── __init__.py
│   ├── idea_analyzer.py
│   ├── scoring_engine.py
│   ├── funding_predictor.py
│   ├── similarity_search.py
│   ├── investor_verdict.py
│   └── market_trends.py
│
├── requirements.txt
└── README.md
⚙️ Installation

Clone the repository:

git clone https://github.com/raj-singh1802/AI-Startup-Evaluator.git

cd AI-Startup-Evaluator

Create a virtual environment:

python -m venv venv

Activate the environment:

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
🔐 Environment Variables

Create a .env file in the project root.

GROQ_API_KEY=your_api_key_here
▶️ Run the Application
streamlit run app/streamlit_app.py

The app will open in your browser.

📊 Dataset Generation

The project includes a script to automatically generate a dataset of AI startups.

Run:

python scripts/generate_startup_dataset.py

This will create a dataset of ~500 startup companies.

📄 Export Startup Evaluation Report

Users can download the full evaluation report including:

Startup analysis

Startup score

Funding probability

Investor verdict

Market trend analysis

🚀 Future Improvements

Possible extensions:

Real-time startup data integration

Startup idea comparison tool

AI startup idea generator

Deployment with Docker

Integration with Crunchbase or YC datasets

👨‍💻 Author

Raj Singh

AI / Machine Learning Engineer

GitHub
https://github.com/raj-singh1802

⭐ If you found this project useful, consider giving it a star!
