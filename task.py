from celery.app import Celery
from datetime import datetime
import os

redis_url = os.getenv("REDIS_URL", "redis://172.15.5.243:6379/0")
app = Celery("tasks", broker=redis_url, backend=redis_url)


@app.task
def dummy_task():
    folder = "/tmp/celery"
    os.makedirs(folder, exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"{folder}/task-{now}.txt", "w") as f:
        f.write("This is a dummy task executed at: " + str(datetime.now()))


if __name__ == "__main__":
    dummy_task.delay()
