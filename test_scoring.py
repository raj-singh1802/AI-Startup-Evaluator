import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.scoring_engine import score_startup

test_cases = [
    ("Strong SaaS AI Healthcare", {
        "industry": "AI Healthcare",
        "target_customers": "Hospitals and Clinics",
        "business_model": "B2B SaaS Subscription",
        "market_potential": "High",
        "competition_level": "Low"
    }),
    ("Weak Food Delivery Clone", {
        "industry": "Food Delivery",
        "target_customers": "General consumers",
        "business_model": "Commission-based marketplace",
        "market_potential": "Medium",
        "competition_level": "High"
    }),
    ("Niche Typewriter Repair", {
        "industry": "Vintage Typewriter Repairs",
        "target_customers": "Typewriter collectors",
        "business_model": "Service-based, hourly billing",
        "market_potential": "Low",
        "competition_level": "Low"
    }),
]

results = []
for name, analysis in test_cases:
    score = score_startup(analysis)
    results.append(f"{name}: {score}/10")

with open("test_results.txt", "w") as f:
    f.write("\n".join(results))

for r in results:
    print(r)
