from tasks import (
    create_task,
    list_tasks,
    complete_task,
    delete_task,
    edit_task
                   )

tasks = []

test_list = [
    {"id": 1, "title": "test1", "completed": False},
    {"id": 2, "title": "test2", "completed": False},
    {"id": 3, "title": "test3", "completed": True},
    {"id": 4, "title": "test4", "completed": True}
] 

create_task(tasks, "learn JSON")
create_task(tasks, "Understand file handling")

list_tasks(tasks)