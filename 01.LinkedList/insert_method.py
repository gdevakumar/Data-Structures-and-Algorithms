from linkedlist import LinkedList

my_linked_list = LinkedList(1)
my_linked_list.append(3)

print('LL before insert():')
my_linked_list.print_list()

my_linked_list.insert(1,2)

print('\nLL after insert(2) in middle:')
my_linked_list.print_list()

my_linked_list.insert(0,0)

print('\nLL after insert(0) at beginning:')
my_linked_list.print_list()

my_linked_list.insert(4,4)

print('\nLL after insert(4) at end:')
my_linked_list.print_list()
