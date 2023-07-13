from queue import Queue

my_queue = Queue(1)
my_queue.enqueue(2)

print(my_queue.dequeue().value)
print(my_queue.dequeue().value)
print(my_queue.dequeue())
