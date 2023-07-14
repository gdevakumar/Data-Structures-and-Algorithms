from doublylinkedlist import DoublyLinkedList

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(3)

print('DLL before insert():')
my_doubly_linked_list.print()


my_doubly_linked_list.insert(1,2)

print('\nDLL after insert(2) in middle:')
my_doubly_linked_list.print()

my_doubly_linked_list.insert(0,0)

print('\nDLL after insert(0) at beginning:')
my_doubly_linked_list.print()

my_doubly_linked_list.insert(4,4)

print('\nDLL after insert(4) at end:')
my_doubly_linked_list.print()