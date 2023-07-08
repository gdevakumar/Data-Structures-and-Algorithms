from linkedlist import LinkedList

my_linked_list = LinkedList(2)
my_linked_list.append(3)

print('Before prepend():')
print('----------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()

my_linked_list.prepend(1)

print('\n\nAfter prepend():')
print('---------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()
