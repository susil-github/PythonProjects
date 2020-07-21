class AppRuntimeError(Exception):
    def __init__(self,data):
        self.data=data;
    def __str__(self):
        return repr(self.data)

try:
    raise AppRuntimeError("this is error on runtime")
except AppRuntimeError as a:
    print("Error : ",a.data)