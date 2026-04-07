import asyncio
import os
from openai import OpenAI
from env.environment import EmailEnv
from env.models import Action

API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

MAX_STEPS = 3
MAX_TOTAL_REWARD = 1.0
SUCCESS_SCORE_THRESHOLD = 0.6

def log_start(task, env, model):
    print(f"[START] task={task}, env={env}, model={model}", flush=True)

def log_step(step, action, reward, done, error):
    print(f"[STEP] step={step}, action={action}, reward={reward}, done={done}", flush=True)

def log_end(success, steps, score, rewards):
    print(f"[END] success={success}, steps={steps}, score={score}, rewards={rewards}", flush=True)

def get_model_action():
    # simple baseline
    return Action(
        classification="spam",
        priority=1,
        reply="ok"
    )

async def main():
    client = None  # temporary fix

    env = EmailEnv()

    rewards = []
    steps_taken = 0

    log_start("email_task", "EmailEnv", MODEL_NAME)

    result = env.reset()

    for step in range(1, MAX_STEPS + 1):
        action = get_model_action()

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

if __name__ == "__main__":
    asyncio.run(main())
