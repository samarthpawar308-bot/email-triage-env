TASKS = [
    {
        "id": "easy",
        "email": "Win a free iPhone now!!! Click here",
        "expected_classification": "spam",
        "expected_priority": 1,
        "expected_reply": ""
    },
    {
        "id": "medium",
        "email": "Client meeting rescheduled to tomorrow. Please confirm.",
        "expected_classification": "urgent",
        "expected_priority": 3,
        "expected_reply": "Acknowledged"
    },
    {
        "id": "hard",
        "email": "We noticed discrepancies in your latest data report. Can you clarify?",
        "expected_classification": "normal",
        "expected_priority": 2,
        "expected_reply": "clarify"
    }
]
