import uuid

class Task:
    def __init__(self, func, args=None, kwargs=None):
        self.id = str(uuid.uuid4())
        self.func = func
        self.args = args or []
        self.kwargs = kwargs or {}

        print(f"[TASK CREATED] id={self.id}, func={func.__name__}, args={self.args}")
    
    def execute(self):
        print(f"[TASK EXECUTE] id={self.id}")
        return self.func(*self.args, **self.kwargs)

def task(func):
    def wrapper(*args, **kwargs):
        return Task(func, args, kwargs)
    return wrapper
