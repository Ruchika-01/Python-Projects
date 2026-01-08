
from job_task_processor_python.core.job import Job
from job_task_processor_python.core.queue import JobQueue


def dummy_task():
    return "ok"


def test_enqueue_and_dequeue():
    queue = JobQueue()
    job = Job(task=dummy_task)

    queue.enqueue(job)
    assert queue.size() == 1

    dequeued_job = queue.dequeue()
    assert dequeued_job == job
    assert queue.is_empty()


def test_dequeue_empty_queue():
    queue = JobQueue()
    job = queue.dequeue()
    assert job is None
