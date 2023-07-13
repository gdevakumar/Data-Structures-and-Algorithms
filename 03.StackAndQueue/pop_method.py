from stack import Stack

my_stack = Stack(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)

print('Stack before pop():')
my_stack.print()

print('\nPopped node:')
print(my_stack.pop().value)

print('\nStack after pop():')
my_stack.print()