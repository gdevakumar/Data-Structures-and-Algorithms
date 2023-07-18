from maxheap import MaxHeap

myheap = MaxHeap()
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(95)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)

myheap.remove()

print(myheap.heap)

myheap.remove()

print(myheap.heap)
