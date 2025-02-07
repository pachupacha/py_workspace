import math

def softmax(scores):
    exps = [math.exp(s) for s in scores]
    total = sum(exps)
    return [e / total for e in exps]

def get_valid_input(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ["y", "n"]:
            return ans
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

parties = [
    {"name": "Union for the Homeland", "seats": 99, "ideology": -0.5, "government": False},
    {"name": "Liberty Advances", "seats": 39, "ideology": 0.9, "government": True},
    {"name": "Republican Proposal", "seats": 37, "ideology": 0.6, "government": True, "gov_sensitivity": 0.5},
    {"name": "Radical Civic Union", "seats": 34, "ideology": 0.0, "government": False},
    {"name": "Federal Coalition", "seats": 23, "ideology": -0.2, "government": False},
    {"name": "Federal Innovation", "seats": 9, "ideology": 0.5, "government": False},
    {"name": "Workers' Left Front - Unity", "seats": 5, "ideology": -1.0, "government": False, "ultra_opposition": True},
    {"name": "Independent Block", "seats": 3, "ideology": 0.0, "government": False},
    {"name": "For Santa Cruz", "seats": 2, "ideology": 0.1, "government": False},
    {"name": "Production and Labour", "seats": 2, "ideology": -0.4, "government": False},
    {"name": "Free Buenos Aires", "seats": 2, "ideology": 0.4, "government": False},
    {"name": "CREO", "seats": 1, "ideology": 0.6, "government": False},
    {"name": "Mendoza Union", "seats": 1, "ideology": 0.0, "government": False}
]

questionnaire = [
    {"text": "Does the law favor businesses?", "type": "base", "weight": 2},
    {"text": "Is the law driven by government?", "type": "base", "weight": 1},
    {"text": "Does the law have a human rights defense approach?", "type": "mod", "orientation": -1, "weight": 0.5},
    {"text": "Does the law benefit vulnerable sectors?", "type": "mod", "orientation": -1, "weight": 0.5},
    {"text": "Does the law increase state intervention in the economy?", "type": "mod", "orientation": -1, "weight": 0.7},
    {"text": "Does the law favor free enterprise?", "type": "mod", "orientation": 1, "weight": 0.7},
    {"text": "Does the law include fiscal austerity measures?", "type": "mod", "orientation": 1, "weight": 0.5},
    {"text": "Does the law increase public spending on health?", "type": "mod", "orientation": -1, "weight": 0.5},
    {"text": "Does the law promote labor reforms that reduce workers' rights?", "type": "mod", "orientation": 1, "weight": 0.7},
    {"text": "Does the law strengthen the executive power?", "type": "mod", "orientation": 0.5, "weight": 0.5},
    {"text": "Does the law weaken democratic institutions?", "type": "mod", "orientation": 0, "weight": 0.5},
    {"text": "Does the law have an environmental approach?", "type": "mod", "orientation": -0.5, "weight": 0.5},
    {"text": "Does the law prioritize national security?", "type": "mod", "orientation": 1, "weight": 0.5},
    {"text": "Does the law centralize power in the capital?", "type": "mod", "orientation": 1, "weight": 0.5},
    {"text": "Does the law contemplate modifications in the justice system?", "type": "mod", "orientation": 0.2, "weight": 0.3},
    {"text": "Does the law promote foreign investment?", "type": "mod", "orientation": 1, "weight": 0.7},
    {"text": "Does the law contemplate educational reforms?", "type": "mod", "orientation": 0, "weight": 0.3},
    {"text": "Does the law favor administrative decentralization?", "type": "mod", "orientation": -1, "weight": 0.5},
    {"text": "Does the law incentivize infrastructure investment?", "type": "mod", "orientation": 0.5, "weight": 0.5},
    {"text": "Does the law promote technological development and innovation?", "type": "mod", "orientation": 0.5, "weight": 0.4},
    {"text": "Does the law establish transparency measures in public management?", "type": "mod", "orientation": -0.5, "weight": 0.5},
    {"text": "Does the law modify the regime of minorities or gender quotas?", "type": "mod", "orientation": -1, "weight": 0.6}
]

print("Answer the following questionnaire (y/n):")
answers = []
for i, q in enumerate(questionnaire, start=1):
    ans = get_valid_input(f"{i}. {q['text']} ")
    answers.append(ans)

for party in parties:
    party["coeff_positive"] = 0
    party["coeff_negative"] = 0
    party["coeff_abstain"] = -0.5

for i, q in enumerate(questionnaire):
    ans = answers[i]
    eff = 1 if ans == "y" else -1
    if q["type"] == "base":
        if i == 0:
            for party in parties:
                party["coeff_positive"] += eff * q["weight"] * party["ideology"]
                party["coeff_negative"] -= eff * q["weight"] * party["ideology"]
        elif i == 1:
            for party in parties:
                mult = party.get("gov_sensitivity", 1)
                if party["government"]:
                    party["coeff_positive"] += eff * q["weight"] * mult
                    party["coeff_negative"] -= eff * q["weight"] * mult
                else:
                    party["coeff_positive"] -= eff * q["weight"] * mult
                    party["coeff_negative"] += eff * q["weight"] * mult
    else:
        if q.get("orientation", 0) != 0:
            for party in parties:
                align = party["ideology"] * q["orientation"]
                party["coeff_positive"] += eff * q["weight"] * align
                party["coeff_negative"] -= eff * q["weight"] * align
        else:
            for party in parties:
                party["coeff_abstain"] += eff * q["weight"]

for party in parties:
    s = softmax([party["coeff_positive"], party["coeff_negative"], party["coeff_abstain"]])
    party["p_positive"], party["p_negative"], party["p_abstain"] = s[0], s[1], s[2]

p_present = 0.9
results = []
total_positive = total_negative = total_abstain = total_present = total_seats = 0

for party in parties:
    seats = party["seats"]
    present = round(seats * p_present)
    votes_positive = round(present * party["p_positive"])
    votes_negative = round(present * party["p_negative"])
    votes_abstain = round(present * party["p_abstain"])
    results.append({"party": party["name"], "seats": seats, "p_positive": party["p_positive"], "votes_positive": votes_positive, "votes_negative": votes_negative, "votes_abstain": votes_abstain})
    total_positive += votes_positive
    total_negative += votes_negative
    total_abstain += votes_abstain
    total_present += present
    total_seats += seats

print("\nVoting results:\n")
for r in results:
    print(f"{r['party']} ({r['seats']} seats):")
    print(f"  Positive probability: {r['p_positive']*100:.1f}%")
    print(f"  Votes - Positive: {r['votes_positive']}, Negative: {r['votes_negative']}, Abstain: {r['votes_abstain']}\n")

print("Total seats:", total_seats)
print("Present:", total_present)
print("Positive votes:", total_positive)
print("Negative votes:", total_negative)
print("Abstentions:", total_abstain)

quorum = (total_seats // 2) + 1
print("Quorum required:", quorum)

votes_cast = total_positive + total_negative
if total_present >= quorum:
    if total_positive >= (votes_cast // 2 + 1):
        final_result = "Law approved"
    else:
        final_result = "Law rejected"
else:
    if total_positive >= (votes_cast // 2 + 1):
        final_result = "Law with MEDIA SANCTION"
    else:
        final_result = "Law rejected"

print("Final result:", final_result)

