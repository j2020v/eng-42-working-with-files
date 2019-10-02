from open_basics import *

#open_read_file_('order.txt')
#open_read_file_using_with('order.txt')

# append_to_file("order.txt", '\nNandos Peri-flamer wings')
#
# write_to_file('orders.txt', 'Pizza')

list_order = ['Sea Bass Grilled', 'Champagne', 'Noodles', 'Rice', 'Sushi']
for item in list_order:
    write_to_file('order.txt', item)
