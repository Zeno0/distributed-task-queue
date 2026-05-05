from collections import deque
import threading

class TaskQueue:
    def __init__(self):
        self.queue = deque()
        self.lock = threading.Lock()

    def push(self, task):
        with self.lock:
            self.queue.append(task)
            print(f"[QUEUE PUSH] Task {task.id} added. Queue size={len(self.queue)}")

    def pop(self):
        with self.lock:
            if self.queue:
                task = self.queue.popleft()
                print(f"[QUEUE POP] Task {task.id} removed. Queue size={len(self.queue)}")
                return task
            return None
