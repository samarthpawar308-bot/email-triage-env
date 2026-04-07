def grade(task, action):
    score = 0.0

    # classification
    if action.classification == task["expected_classification"]:
        score += 0.4

    # priority
    if action.priority == task["expected_priority"]:
        score += 0.3

    # reply (partial match)
    if task["expected_reply"].lower() in action.reply.lower():
        score += 0.3

    return min(score, 1.0)
