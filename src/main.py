from tasks import (
    create_task,
    list_tasks,
    complete_task,
    delete_task,
    edit_task
)
from storage import save_tasks, load_tasks

tasks = load_tasks()