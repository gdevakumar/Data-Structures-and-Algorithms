# We can use either List or LinkedList to represent a Stack. Here, we are using LinkedList to implement Stack

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        node = Node(value)
        self.top = node
        self.height = 1

    def print(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        node = Node(value)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        if self.height == 1:
            self.top = None
        else:
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp