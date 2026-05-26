import json

class Memory:
    def __init__(self, file_path="memory.json"):
        self.file_path = file_path
        self.data = self.load()

    def load(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except:
            return {"insights": [], "strategy": ""}

    def save(self, new_data):
        """
        Saves new insights or strategy updates.
        """
        if "insights" in new_data:
            self.data["insights"].extend(new_data["insights"])

        if "strategy" in new_data:
            self.data["strategy"] = new_data["strategy"]

        with open(self.file_path, "w") as f:
            json.dump(self.data, f, indent=4)

        return {"status": "saved", "memory": self.data}

    def get(self):
        return self.data
