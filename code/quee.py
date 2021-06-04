from queue import Queue
from threading import Thread

TODO = Queue()


class Worker(Thread):
    def run(self):
        while True:
            # Remove and return an item from the queue.
            job = TODO.get()

            # Execute work
            print(f'Will do the work: {job}')

            # Indicate that a formerly enqueued task is complete.
            TODO.task_done()


def spawn_worker(count=1):
    for i in range(count):
        Worker().start()


if __name__ == '__main__':
    spawn_worker(3)

    TODO.put('ping')
    TODO.put('ls -la')
    TODO.put('echo "hello world"')
    TODO.put('cat /etc/passwd')

    # wait to complete all tasks
    TODO.join()
