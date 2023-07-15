from hashtable import HashTable

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)

print('Bolts:', my_hash_table.get_item('bolts'))
print('Washers:', my_hash_table.get_item('washers'))
print('Lumber:', my_hash_table.get_item('lumber'))