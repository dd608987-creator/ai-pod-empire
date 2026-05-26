import redis
import json

class AutomationCloud:
    def __init__(self):
        self.redis = redis.Redis()

    def enqueue(self, task_name, params):
        task = {
            "task": task_name,
            "params": params
        }
        self.redis.lpush("task_queue", json.dumps(task))
        return {"status": "queued", "task": task_name}

    def dequeue(self):
        task = self.redis.rpop("task_queue")
        if not task:
            return {"status": "empty"}
        return json.loads(task)

    def queue_length(self):
        return self.redis.llen("task_queue")
