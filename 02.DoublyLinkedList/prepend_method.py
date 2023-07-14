from doublylinkedlist import DoublyLinkedList

my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(3)

print('Before prepend():')
print('----------------')
print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length, '\n')
print('Doubly Linked List:')
my_doubly_linked_list.print()

my_doubly_linked_list.prepend(1)

print('\n\nAfter prepend():')
print('---------------')
print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length, '\n')
print('Doubly Linked List:')
my_doubly_linked_list.print()