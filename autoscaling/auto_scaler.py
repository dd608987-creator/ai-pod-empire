import redis

class AutoScaler:
    def __init__(self, logger=None):
        self.redis = redis.Redis()
        self.logger = logger

    def monitor(self):
        """
        Checks how many tasks are waiting in the queue.
        """
        queue_length = self.redis.llen("task_queue")
        return queue_length

    def scale(self):
        """
        Decides whether to scale up or down based on queue size.
        """
        queue_length = self.monitor()

        if queue_length > 100:
            return {
                "action": "scale_up",
                "workers": 5,
                "reason": "High task load"
            }

        if queue_length < 10:
            return {
                "action": "scale_down",
                "workers": 2,
                "reason": "Low task load"
            }

        return {
            "action": "stable",
            "reason": "Normal load"
        }
