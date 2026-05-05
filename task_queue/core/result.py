class ResultBackend:
    def __init__(self):
        self.results = {}

    def store(self, task_id, result):
        self.results[task_id] = result
        print(f"[RESULT STORE] Task {task_id} → {result}")

    
    def get(self, task_id):
        result = self.results.get(task_id)
        print(f"[RESULT GET] Task {task_id} → {result}")
        return result
