from queue import Queue

my_queue = Queue(1)

print('Queue before enqueue(2):')
my_queue.print()

my_queue.enqueue(2)

print('\nQueue after enqueue(2):')
my_queue.print()