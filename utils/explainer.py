SUSPICIOUS_WORDS = [
    "free",
    "winner",
    "won",
    "claim",
    "click",
    "urgent",
    "immediately",
    "offer",
    "bonus",
    "bitcoin",
    "bank",
    "verify",
    "password",
    "account",
    "gift",
    "prize",
    "limited",
    "congratulations",
    "reward"
]


def highlight_keywords(text):

    found = []

    lower = text.lower()

    for word in SUSPICIOUS_WORDS:

        if word in lower:
            found.append(word)

    return found