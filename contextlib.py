@contextlib.contextmanager
def open_func(file_name):
    print("open file:",file_name,"in __enter__")
    file_handler = open(file_name,'r')

    yield file_handler

#exit方法
    print("close file:",file_name,"in__exit__")
    file_handler.close()

#使用实例
with open_func("test.txt") as file_in:
    for line in file_in:
        print(line)
        break
