import datetime

tasks = []

def create_task(tasks: list[dict], title: str) -> dict:
    if not isinstance(title, str):
        raise TypeError("Title must be a string")

    name = title.strip()
    if not name:
        raise ValueError("Task title cannot be empty or contain only whitespace") 

    created_at = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    
    task = {
        "id": max((task["id"] for task in tasks), default=0) + 1,
        "title": name,
        "completed": False,
        "created_at": created_at,
    }
    tasks.append(task)
    return task

def list_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print("The task list is empty")
        return
    print(f"Your tasks ({len(tasks)}): \n")
    for task in tasks:
        print(f"[{task['id']}] {task['title']} - {'Incomplete' if not task['completed'] else 'Complete'}")

def complete_task(tasks: list[dict], task_id: int) -> dict:
    if not isinstance(task_id, int) or isinstance(task_id, bool):
        raise TypeError("Id must be of type integer")
    for task in tasks:
        if task_id == task["id"]:
            if task["completed"]:
                return {
                    "status": "already_completed",
                    "message": "Task was already completed",
                    "task_id": task_id
                }
            task["completed"] = True
            return {
                "status": "task_completed",
                "message": "Task was completed",
                "task_id": task_id
            }
    return {
        "status": "not_found",
        "message": "Task not found",
        "task_id": task_id
    }

def delete_task(tasks: list[dict], task_id: int) -> dict:
    if not isinstance(task_id, int) or isinstance(task_id, bool):
        raise TypeError("Id must be an integer")
    if not tasks:
        return {"status": "empty_list",
                "message": "Task list is empty",
                "task_id": task_id
        }
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"status": "deleted_task",
                    "message": "Task has been deleted",
                    "task_id": task_id
            }
    return {"status": "not_found",
            "message": "Task not found",
            "task_id": task_id
    }

test_list = [
    {"id": 1, "title": "test1", "completed": False},
    {"id": 2, "title": "test2", "completed": False},
    {"id": 3, "title": "test3", "completed": True},
    {"id": 4, "title": "test4", "completed": True}
]
