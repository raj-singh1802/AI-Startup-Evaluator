def extract_level(text):
    """
    Extract High / Medium / Low from LLM output text
    """
    text = text.lower()

    if "high" in text:
        return "high"
    elif "medium" in text:
        return "medium"
    elif "low" in text:
        return "low"
    else:
        return "medium"


def score_startup(analysis):

    score_map = {
        "high": 9,
        "medium": 6,
        "low": 3
    }

    market = score_map[extract_level(analysis["market_potential"])]
    competition = score_map[extract_level(analysis["competition_level"])]

    # invert competition
    competition = 10 - competition

    # business model bonus
    model_text = analysis["business_model"].lower()

    if "subscription" in model_text or "saas" in model_text:
        model_score = 8
    elif "marketplace" in model_text:
        model_score = 7
    else:
        model_score = 5

    final_score = (market * 0.5) + (competition * 0.3) + (model_score * 0.2)

    return round(final_score, 2)


def startup_recommendation(score):

    if score >= 8:
        return "🚀 Strong startup idea. High potential."

    elif score >= 6:
        return "⚡ Moderate potential. Needs differentiation."

    else:
        return "⚠️ High risk startup idea."