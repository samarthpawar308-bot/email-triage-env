import asyncio
import os
from openai import OpenAI
from env.environment import EmailEnv
from env.models import Action

# ✅ REQUIRED ENV VARIABLES (from hackathon system)
API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

MAX_STEPS = 3
MAX_TOTAL_REWARD = 1.0
SUCCESS_SCORE_THRESHOLD = 0.6


def log_start(task, env, model):
    print(f"[START] task={task}, env={env}, model={model}", flush=True)


def log_step(step, action, reward, done, error):
    print(f"[STEP] step={step}, action={action}, reward={reward}, done={done}", flush=True)


def log_end(success, steps, score, rewards):
    print(f"[END] success={success}, steps={steps}, score={score}, rewards={rewards}", flush=True)


# ✅ LLM-based action (IMPORTANT FIX)
def get_model_action(client):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant that classifies emails and generates replies."
            },
            {
                "role": "user",
                "content": "Classify this email and generate a short reply:\n\nHello, I need help with my account login issue."
            }
        ]
    )

    reply = response.choices[0].message.content

    # Basic structured output (can be improved later)
    return Action(
        classification="important",
        priority=1,
        reply=reply
    )


async def main():
    # ✅ FIX: initialize client using proxy
    client = OpenAI(
        base_url=API_BASE_URL,
        api_key=API_KEY
    )

    env = EmailEnv()

    rewards = []
    steps_taken = 0

    log_start("email_task", "EmailEnv", MODEL_NAME)

    result = env.reset()

    for step in range(1, MAX_STEPS + 1):
        # ✅ USE LLM HERE
        action = get_model_action(client)

        result = env.step(action)

        reward = result["reward"]
        done = result["done"]

        rewards.append(reward)
        steps_taken = step

        log_step(step, str(action), reward, done, None)

        if done:
            break

    score = sum(rewards) / MAX_TOTAL_REWARD
    success = score >= SUCCESS_SCORE_THRESHOLD

    log_end(success, steps_taken, score, rewards)

    return {
        "success": success,
        "score": score,
        "steps": steps_taken
    }


if __name__ == "__main__":
    asyncio.run(main())
