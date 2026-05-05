import time

class Worker:
    def __init__(self, queue, result_backend):
        self.queue = queue
        self.result_backend = result_backend
        self.running = True

    def start(self):
        print("[WORKER] Started worker loop")

        while self.running:
            task = self.queue.pop()
            if task:
                print(f"[WORKER] Picked task {task.id}")

                try:
                    result = task.execute()
                    print(f"[WORKER] Completed task {task.id} → result={result}")
                    self.result_backend.store(task.id, result)
                except Exception as e:
                    print(f"[WORKER ERROR] Task {task.id} failed → {e}")
                    self.result_backend.store(task.id, str(e))
            else:
                time.sleep(0.1)