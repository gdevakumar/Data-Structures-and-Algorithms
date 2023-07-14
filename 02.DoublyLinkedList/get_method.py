from doublylinkedlist import DoublyLinkedList

my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)

print('Get node from first half of DLL:')
print(my_doubly_linked_list.get_value(1).value)

print('\nGet node from second half of DLL:')
print(my_doubly_linked_list.get_value(2).value)