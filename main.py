from task_queue.core.task import task
from task_queue.core.queue import TaskQueue
from task_queue.core.worker import Worker
from task_queue.core.result import ResultBackend

import threading
import time

@task
def multiply(x,y):
    return x*y
print("[MAIN] Starting system...")
queue = TaskQueue()
backend = ResultBackend()

worker = Worker(queue, backend)

threading.Thread(target = worker.start, daemon = True).start()

t = multiply(5,6)
print("[MAIN] Submitting task...")
queue.push(t)

time.sleep(1)
print("[MAIN] Fetching result...")
print("Result:", backend.get(t.id))