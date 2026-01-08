def success_task():
    return "Task executed successfully"


def failure_task():
    raise RuntimeError("Task failed intentionally")
