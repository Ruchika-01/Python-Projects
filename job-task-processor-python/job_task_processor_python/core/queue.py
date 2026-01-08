from collections import deque
from typing import Optional
from job_task_processor_python.core.job import Job



class JobQueue:
    """
    FIFO queue for managing jobs.
    """

    def __init__(self):
        self._queue = deque()

    def enqueue(self, job: Job) -> None:
        self._queue.append(job)

    def dequeue(self) -> Optional[Job]:
        if not self._queue:
            return None
        return self._queue.popleft()

    def is_empty(self) -> bool:
        return len(self._queue) == 0

    def size(self) -> int:
        return len(self._queue)

    def __repr__(self):
        return f"<JobQueue size={len(self._queue)}>"
