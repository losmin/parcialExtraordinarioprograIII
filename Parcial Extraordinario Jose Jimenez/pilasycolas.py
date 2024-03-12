def create_queue() -> list:
    queue = []
    return queue

def enqueue(queue: list, value) -> None:
    queue.append(value)

def dequeue(queue: list) -> any:
    return queue.pop(0)

def is_empty(queue: list) -> bool:
    return len(queue) == 0

queue = create_queue()
enqueue(queue, "a")
enqueue(queue, "b")
enqueue(queue, "c")

print(queue)

front_value = dequeue(queue)
print(front_value)

print(queue)

print(is_empty(queue))