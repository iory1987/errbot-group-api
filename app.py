from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from celery.result import AsyncResult
import task
from redis import Redis
from redis.lock import Lock as RedisLock

app = FastAPI()
redis_instance = Redis.from_url(task.redis_url)
lock = RedisLock(redis_instance, name="lock")

tasks_status = []


class TaskOut(BaseModel):
    id: str
    status: str


@app.get("/start")
def start_task() -> TaskOut:
    task_id = task.dummy_task.apply_async()
    tasks_status.append({"id": task_id.id})
    return TaskOut(id=task_id.id, status=task_id.status)


@app.get("/tasks")
def get_tasks_status() -> List:
    return tasks_status


@app.get("/tasks/{task_id}")
def get_task_status(task_id: str) -> TaskOut:

    try:
        task_result = task.app.AsyncResult(task_id)
        return TaskOut(id=task_id, status=task.state)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
