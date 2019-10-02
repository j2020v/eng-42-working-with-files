# Here we define our open/close functions
def open_read_file(file):
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



