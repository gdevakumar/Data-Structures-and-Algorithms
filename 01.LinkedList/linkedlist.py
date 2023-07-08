class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print(None)

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            print("LinkedList is empty!")
            return None
        temp = self.head
        before = self.head
        while temp.next:
            before = temp
            temp = temp.next
        before.next = None
        self.tail = before
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            print("LinkedList is empty!")
            return None
        temp = self.head
        self.head = temp.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get_value(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
        else:
            temp = self.head
            before = temp
            for _ in range(index):
                before = temp
                temp = temp.next
            before.next = new_node
            new_node.next = temp
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        before = self.get_value(index-1)
        temp = before.next
        before.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        if self.length <= 1:
            return
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

