import os
import sys

# Allow importing from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import plotly.graph_objects as go

from src.idea_analyzer import analyze_startup
from src.scoring_engine import score_startup, startup_recommendation
from src.similarity_search import find_similar_startups
from src.investor_verdict import generate_investor_verdict
from src.market_trends import analyze_market_trend
from src.funding_predictor import predict_funding_probability


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(page_title="AI Startup Evaluator", layout="wide")


# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("⚙️ Controls")

st.sidebar.markdown("### Evaluation Settings")

show_similar = st.sidebar.checkbox("Show Similar Startups", value=True)
show_verdict = st.sidebar.checkbox("Show AI Investor Verdict", value=True)
show_trends = st.sidebar.checkbox("Show Market Trend Analysis", value=True)

st.sidebar.markdown("---")

st.sidebar.info(
    "AI Startup Evaluator\n\n"
    "Built using LLM + Vector Search + Analytics"
)


# ---------------------------------------------------
# UI STYLING
# ---------------------------------------------------

st.markdown("""
<style>
.metric-card {
    background: linear-gradient(135deg, #1f77b4, #6a11cb);
    padding: 20px;
    border-radius: 10px;
    color: white;
    text-align: center;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# MAIN TITLE
# ---------------------------------------------------

st.title("🚀 AI Startup Evaluator")

idea = st.text_area("Enter your startup idea")


# ---------------------------------------------------
# EVALUATION BUTTON
# ---------------------------------------------------

if st.button("Evaluate Startup"):

    if idea.strip() == "":
        st.warning("Please enter a startup idea.")
        st.stop()

    with st.spinner("🤖 AI analyzing startup potential..."):

        # ---------------------------------------------------
        # CORE ANALYSIS
        # ---------------------------------------------------

        analysis = analyze_startup(idea)

        score = score_startup(analysis)

        recommendation = startup_recommendation(score)

        funding_probability = predict_funding_probability(analysis)

        similar = find_similar_startups(idea)

        verdict = generate_investor_verdict(idea, analysis, score)

        trend = analyze_market_trend(idea, analysis)


        # ---------------------------------------------------
        # METRIC CALCULATIONS FOR RADAR
        # ---------------------------------------------------

        market = analysis["market_potential"].lower()
        competition = analysis["competition_level"].lower()

        score_map = {"high": 9, "medium": 6, "low": 3}

        market_score = score_map.get(market, 6)

        competition_score = 10 - score_map.get(competition, 6)

        funding_score = funding_probability / 10

        innovation_score = score

        risk_score = 10 - score


        categories = [
            "Market Potential",
            "Competition Advantage",
            "Funding Potential",
            "Innovation",
            "Risk"
        ]

        values = [
            market_score,
            competition_score,
            funding_score,
            innovation_score,
            risk_score
        ]


        # ---------------------------------------------------
        # RADAR CHART
        # ---------------------------------------------------

        fig_radar = go.Figure()

        fig_radar.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Startup Metrics'
        ))

        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
            showlegend=False,
            height=400
        )


        # ---------------------------------------------------
        # SCORE GAUGE
        # ---------------------------------------------------

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={'text': "Startup Score"},
            gauge={
                'axis': {'range': [0, 10]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 4], 'color': "red"},
                    {'range': [4, 7], 'color': "orange"},
                    {'range': [7, 10], 'color': "green"}
                ]
            }
        ))


        # ---------------------------------------------------
        # DASHBOARD LAYOUT
        # ---------------------------------------------------

        col1, col2 = st.columns(2)


        # ---------------------------------------------------
        # LEFT PANEL
        # ---------------------------------------------------

        with col1:

            st.subheader("Startup Analysis")

            for key, value in analysis.items():
                st.write(f"**{key.replace('_',' ').title()}**")
                st.write(value)


            if show_similar:

                st.subheader("Similar Startups")

                for s in similar:

                    if isinstance(s, dict):

                        st.markdown(
                            f"""
                            **{s['name']}**

                            {s['description']}
                            """
                        )

                    else:
                        st.success(s)


        # ---------------------------------------------------
        # RIGHT PANEL
        # ---------------------------------------------------

        with col2:

            st.subheader("Startup Score")

            st.plotly_chart(fig_gauge, use_container_width=True)

            st.progress(score / 10)

            st.markdown(
                f"""
                <div class="metric-card">
                    <h2>Startup Score</h2>
                    <h1>{score} / 10</h1>
                </div>
                """,
                unsafe_allow_html=True
            )


            st.subheader("💰 Funding Probability")

            st.metric(
                "Chance of VC Funding",
                f"{funding_probability}%"
            )


            st.subheader("Recommendation")

            st.write(recommendation)


            st.subheader("📊 Startup Metrics Overview")

            st.plotly_chart(fig_radar, use_container_width=True)


        # ---------------------------------------------------
        # INVESTOR VERDICT
        # ---------------------------------------------------

        if show_verdict:

            st.subheader("🧠 AI Investor Verdict")

            st.write(verdict)


        # ---------------------------------------------------
        # MARKET TREND ANALYSIS
        # ---------------------------------------------------

        if show_trends:

            st.subheader("📈 Market Trend Analysis")

            st.write(trend)


        # ---------------------------------------------------
        # DOWNLOAD REPORT
        # ---------------------------------------------------

        report = f"""
Startup Idea: {idea}

Industry: {analysis["industry"]}

Target Customers: {analysis["target_customers"]}

Business Model: {analysis["business_model"]}

Market Potential: {analysis["market_potential"]}

Competition Level: {analysis["competition_level"]}

Startup Score: {score}/10

Funding Probability: {funding_probability}%

Recommendation: {recommendation}

Investor Verdict:
{verdict}

Market Trend:
{trend}
"""

        st.download_button(
            label="📄 Download Evaluation Report",
            data=report,
            file_name="startup_evaluation.txt",
            mime="text/plain"
        )


# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.caption(
    "AI Startup Evaluator • Built with LLMs, FAISS, and Streamlit"
)