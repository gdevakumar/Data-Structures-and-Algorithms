from doublylinkedlist import DoublyLinkedList

my_doubly_linked_list = DoublyLinkedList(11)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(7)

print('DLL before set_value():')
my_doubly_linked_list.print()

my_doubly_linked_list.set_value(1,4)

print('\nDLL after set_value():')
my_doubly_linked_list.print()
