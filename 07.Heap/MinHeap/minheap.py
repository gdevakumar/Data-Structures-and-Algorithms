class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        curr = len(self.heap) - 1
        while curr > 0 and self.heap[curr] < self.heap[self._parent(curr)]:
            self._swap(curr, self._parent(curr))
            curr = self._parent(curr)

    def _sink_down(self, index):
        min_index = index
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
                min_index = left
            if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
                min_index = right
            if index != min_index:
                self._swap(index, min_index)
                index = min_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return min_value