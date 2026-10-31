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

titles_list = [
    "",
    "  test  ",
    "python",
    "     ",
    None,
    123
]

for title in titles_list:
    try:
        print(create_task(tasks, title))
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")

list_tasks([])
list_tasks([{'id': 1, 'title': 'test', 'completed': False, 'created_at': '2026-10-31T12:47:37+00:00'}])
test_list = [
    {'id': 1, 'title': 'test', 'completed': False, 'created_at': '2026-10-31T12:47:37+00:00'},
    {'id': 2, 'title': 'test2', 'completed': True, 'created_at': '2026-10-31T12:47:37+00:00'},
    {'id': 3, 'title': 'test3', 'completed': False, 'created_at': '2026-10-31T12:47:37+00:00'}
]
list_tasks(test_list)
