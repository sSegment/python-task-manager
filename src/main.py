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

titles_list = [
    "python",
    "  test  ",
    "",
    "     ",
    None,
    123
]

for title in titles_list:
    try:
        print(create_task(tasks, title))
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")

