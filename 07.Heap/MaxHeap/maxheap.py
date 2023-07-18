"""
Generally, Heaps are implemented in a List format. We are using zero-based indexing for heap here.
"""


class MaxHeap:
    def __init__(self):
        self.heap = []

    # Helper Methods
    def _left_child(self, index):
        idx = 2 * index + 1
        return idx

    def _right_child(self, index):
        idx = 2 * index + 2
        return idx

    def _parent(self, index):
        idx = (index-1)//2
        return idx

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        curr = len(self.heap) - 1
        while curr > 0 and self.heap[curr] > self.heap[self._parent(curr)]:
            self._swap(curr, self._parent(curr))
            curr = self._parent(curr)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value

    def _sink_down(self, index):
        max_index = index
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
                max_index = left
            if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
                max_index = right
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
