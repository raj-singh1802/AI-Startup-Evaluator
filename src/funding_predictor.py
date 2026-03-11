import random


def predict_funding_probability(analysis):

    score = 0

    market = analysis["market_potential"].lower()
    competition = analysis["competition_level"].lower()

    if "high" in market:
        score += 40
    elif "medium" in market:
        score += 25
    else:
        score += 10

    if "low" in competition:
        score += 30
    elif "medium" in competition:
        score += 15
    else:
        score += 5

    # small randomness
    score += random.randint(5, 15)

    return min(score, 95)