🚀 AI Startup Evaluator

An AI-powered platform that evaluates startup ideas using Large Language Models, vector similarity search, and scoring models to simulate how venture capital firms assess startups.

The system analyzes a startup idea, predicts funding potential, finds similar startups, and generates an investor-style evaluation report.

📸 Dashboard Preview
Startup Evaluation Dashboard

Startup Analysis

Startup Score

Startup Metrics Radar Chart

✨ Features
🤖 AI Startup Idea Analysis

Uses an LLM to analyze startup ideas and extract:

Industry

Target customers

Business model

Market potential

Competition level

📊 Startup Scoring Engine

Evaluates startup ideas based on:

Market potential

Competitive advantage

Innovation potential

Risk level

💰 Funding Probability Predictor

Predicts the likelihood of venture capital funding based on startup characteristics.

🔎 Similar Startup Detection

Uses:

Sentence Transformers

FAISS Vector Search

to identify similar startups from the dataset.

🧠 AI VC Investor Verdict

Generates a venture capitalist-style evaluation describing:

Strengths

Risks

Investment viability

📈 Market Trend Analysis

Analyzes the industry growth potential and market demand for the startup idea.

📊 Interactive Dashboard

Built using Streamlit, featuring:

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

Activate it:

Windows

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
🔐 Environment Variables

Create a .env file in the project root:

GROQ_API_KEY=your_api_key_here
▶️ Run the Application
streamlit run app/streamlit_app.py

The app will open automatically in your browser.

📊 Dataset Generation

The project includes a script to generate a dataset of AI startups.

Run:

python scripts/generate_startup_dataset.py

This will generate ~500 startup entries for similarity search.

📄 Export Startup Evaluation Report

Users can download a full evaluation report including:

Startup analysis

Startup score

Funding probability

Investor verdict

Market trend analysis

🚀 Future Improvements

Possible extensions include:

Real-time startup database integration

Startup idea comparison tool

AI startup idea generator

Docker deployment

Integration with Crunchbase / YC datasets

👨‍💻 Author

Raj Singh

AI / Machine Learning Engineer

GitHub:
https://github.com/raj-singh1802

⭐ If you found this project useful, consider giving it a star.
