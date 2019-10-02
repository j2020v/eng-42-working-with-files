# Here we define our open/close functions
def open_read_file_(file):
    try:
        opened_file = open(file)  # r = read
        #print(type(file))
        file_lines_list = opened_file.readlines()  # something we can work with
        print(file_lines_list)

        for line in file_lines_list:
            print(line.rstrip('/n'))

        opened_file.close()  # This is the method we add, otherwise file is locked and cannot be changed

    except FileNotFoundError as errmsg:
        print('File cannot be found. Please check your inputs', errmsg)
        raise
    #except:
    #   print('There was been an error. PANIC!!!')

def open_read_file_using_with(file):
    try:
        with open(file, 'r') as open_file: #does not need to close method
            for line in open_file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError as errmsg:
        print('There has been a syntax error', errmsg)
        raise
    finally:
        print('\n Execution_completed')


# def append_to_file(file, order_item):
#     try:
#         opened_file = open(file, 'w') # w = write
#         opened_file.write(order_item)
#
#         opened_file.close()
#     except FileNotFoundError:
#         print('File no found')

def write_to_file(file, order_item):
    try:
        with open(file, 'a') as opened_file: # a = append
            opened_file.write(order_item + '\n') # \n allocates it to a new line
    except FileNotFoundError:
        print('File not found')

