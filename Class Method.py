import contextlib

#打开文件操作
class Open:
    def __init__(self,file_name):
        self.file_name = file_name
        self.file_handler = None
        return

    def __enter__(self):
        print("enter",self.file_name)
        self.file_handler = open(self.file_name,'r')
        return self.file_handler

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit",exc_type,exc_val,exc_tb)
        if self.file_handler:
            self.file_handler.close()
        return True

#使用实例
with Open("test.txt") as file_in:
    for line in file_in:
        print(line)
        raise ZeroDivisionError   #抛出一个异常
