class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if len(self.stack) < 1:
            print('Stack is empty!')
            return None
        return self.stack.pop()

    def peek(self):
        if len(self.stack) < 1:
            print('Stack is empty!')
            return None
        return self.stack[-1]

s = Stack()

s.push(4)
s.push(14)
s.push(43)

print(s.stack)      # [4, 14, 43]
last = s.pop()
print(last)         # 43
print(s.stack)      # [4, 14]
print(s.peek())     # 14
s.pop()
s.pop()
print(s.peek())     # None
