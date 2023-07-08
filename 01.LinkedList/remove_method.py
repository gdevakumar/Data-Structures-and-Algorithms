from linkedlist import LinkedList

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print('LL before remove():')
my_linked_list.print_list()

print('\nRemoved node: ', end='')
print(my_linked_list.remove(2).value)
print('LL after remove() in middle:')
my_linked_list.print_list()

print('\nRemoved node: ', end='')
print(my_linked_list.remove(0).value)
print('LL after remove() of first node:')
my_linked_list.print_list()

print('\nRemoved node: ', end='')
print(my_linked_list.remove(2).value)
print('LL after remove() of last node:')
my_linked_list.print_list()
