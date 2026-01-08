from job_task_processor_python.core.job import Job
from job_task_processor_python.core.queue import JobQueue
from job_task_processor_python.core.worker import Worker
from job_task_processor_python.tasks import success_task, failure_task


if __name__ == "__main__":
    queue = JobQueue()
    worker = Worker(queue)

    job1 = Job(task=success_task)
    job2 = Job(task=failure_task, max_retries=1)

    queue.enqueue(job1)
    queue.enqueue(job2)

    while not queue.is_empty():
        completed_job = worker.process_next_job()
        print(completed_job)
