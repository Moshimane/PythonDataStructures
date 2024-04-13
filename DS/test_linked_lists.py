import DS.linkedlist as linked_list

ls = linked_list.LinkedList()

print('add 4 values to the start of the list')
ls.add_first(5)
ls.add_first(3)
ls.add_first(10)
ls.add_first(5)
ls.print_list()

print('add -7 at index 2')
ls.add_at_index(-7, 2)
ls.print_list()
print('add 19 to the end of the list')
ls.add_last(19)
ls.print_list()

print('Reverse the list')
ls.reverse_list()
ls.print_list()

print('Check if 12 is in the list')
print(ls.check_exist(12))

print('remove the first item from the list')
ls.remove_first()
ls.print_list()

print('remove the last item from the list')
ls.remove_last()
ls.print_list()


