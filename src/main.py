import datetime

tasks = []

def create_task(title):
    created_at = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    task = {
        "id": max((task["id"] for task in tasks), default=0) + 1,
        "title": title,
        "completed": False,
        "created_at": created_at,
    }
    tasks.append(task)
    return task

print(create_task("python"))
print(create_task("test"))