# env/graders.py

def clamp(score: float) -> float:
    """
    Ensure score is strictly between (0, 1)
    """
    return max(0.01, min(0.99, score))


def easy_grader(output, expected):
    score = 0.0

    # classification match
    if output.classification == expected["expected_classification"]:
        score += 0.4

    # priority match
    if output.priority == expected["expected_priority"]:
        score += 0.3

    # reply partial match
    if expected["expected_reply"].lower() in output.reply.lower():
        score += 0.3

    return clamp(score)


def medium_grader(output, expected):
    score = 0.0

    if output.classification == expected["expected_classification"]:
        score += 0.5

    if output.priority == expected["expected_priority"]:
        score += 0.2

    if expected["expected_reply"].lower() in output.reply.lower():
        score += 0.3

    return clamp(score)


def hard_grader(output, expected):
    score = 0.0

    if output.classification == expected["expected_classification"]:
        score += 0.3

    if output.priority == expected["expected_priority"]:
        score += 0.3

    if expected["expected_reply"].lower() in output.reply.lower():
        score += 0.4

    return clamp(score)
