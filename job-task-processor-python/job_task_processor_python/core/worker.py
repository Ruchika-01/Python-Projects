from job_task_processor_python.core.job import JobStatus
from job_task_processor_python.core.queue import JobQueue


class Worker:
    """
    Single-threaded worker that processes jobs from a queue.
    """

    def __init__(self, queue: JobQueue):
        self.queue = queue

    def process_next_job(self):
        job = self.queue.dequeue()

        if job is None:
            return None

        job.mark_running()

        try:
            result = job.task()
            job.mark_success(result)
        except Exception as exc:
            job.increment_retry()

            if job.can_retry():
                job.status = JobStatus.PENDING
                self.queue.enqueue(job)
            else:
                job.mark_failed(exc)

        return job
