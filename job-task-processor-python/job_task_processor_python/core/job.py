from enum import Enum
import uuid
from typing import Callable, Any


class JobStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class Job:
    def __init__(self, task: Callable[..., Any], max_retries: int = 0):
        self.id = str(uuid.uuid4())
        self.task = task
        self.status = JobStatus.PENDING
        self.retries = 0
        self.max_retries = max_retries
        self.result = None
        self.error = None

    def mark_running(self):
        self.status = JobStatus.RUNNING

    def mark_success(self, result: Any):
        self.status = JobStatus.SUCCESS
        self.result = result

    def mark_failed(self, error: Exception):
        self.status = JobStatus.FAILED
        self.error = str(error)

    def can_retry(self) -> bool:
        return self.retries < self.max_retries

    def increment_retry(self):
        self.retries += 1

    def __repr__(self):
        return (
            f"<Job id={self.id} "
            f"status={self.status.value} "
            f"retries={self.retries}/{self.max_retries}>"
        )
