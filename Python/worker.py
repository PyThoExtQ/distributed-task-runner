from queue import Queue

task_queue = Queue()

def worker():
    while not task_queue.empty():
        task = task_queue.get()
        print("Running:", task)
