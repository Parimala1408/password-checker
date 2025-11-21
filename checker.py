import json
from pathlib import Path

BREACH_LIST = Path("breached.txt")
REPORT = Path("report.json")

def load_breach_list():
    if not BREACH_LIST.exists():
        return []
    return [p.strip() for p in BREACH_LIST.read_text().splitlines()]

def strength(password):
    length = len(password)
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    symbol = any(not c.isalnum() for c in password)

    score = sum([upper, lower, digit, symbol]) * 25

    if length < 8:
        score -= 25

    score = max(0, min(score, 100))

    return score

def breached(password, breach_list):
    return password.lower() in [b.lower() for b in breach_list]

def analyze(password):
    def suggestions(password):
    sug = []
    if len(password) < 12:
        sug.append("Use at least 12 characters.")
    if password.islower() or password.isupper():
        sug.append("Mix uppercase and lowercase letters.")
    if not any(c.isdigit() for c in password):
        sug.append("Add numbers.")
    if password.isalnum():
        sug.append("Add special characters (!, @, #, etc.)")
    return sug

    breach_db = load_breach_list()
    result = {
        "password": password,
        "strength": strength(password),
"is_breached": breached(password, breach_db),
"suggestions": suggestions(password)

    }
    REPORT.write_text(json.dumps(result, indent=2))
    print("Report saved:", REPORT)
    return result

if __name__ == "__main__":
    p = input("Enter password to check: ").strip()
    analyze(p)
