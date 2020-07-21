try:
    a=10
    b=2
    c=a/b
    print("value is ",c)
except (ArithmeticError,AssertionError):
    print("the no is not divisible by Zero..")
else:
    print("the no is divisible ....")
finally:
    print("this is finally block....")