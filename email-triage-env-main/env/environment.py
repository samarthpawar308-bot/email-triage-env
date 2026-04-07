from env.models import Observation, Action
from env.tasks import TASKS
from env.graders import grade

class EmailEnv:

    def __init__(self):
        self.current_task = None
        self.done = False

    def reset(self):
        import random
        self.current_task = random.choice(TASKS)
        self.done = False

        return {
            "observation": Observation(
                email=self.current_task["email"]
            ),
            "reward": 0.0,
            "done": False,
            "info": {}
        }

    def step(self, action: Action):
        if self.done:
            return None

        score = grade(self.current_task, action)
        self.done = True

        return {
            "observation": Observation(
                email=self.current_task["email"],
                last_action=str(action)
            ),
            "reward": score,
            "done": True,
            "info": {"task": self.current_task["id"]}
        }

    def state(self):
        return self.current_task
