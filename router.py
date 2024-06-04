from typing import Annotated

from fastapi import APIRouter, Depends

from repo import TaskRepository
from schemas import STaskAdd, STask, STackID

router = APIRouter(
    prefix="/tasks",
    tags=["Задания-дела..."]
)


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STackID:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
