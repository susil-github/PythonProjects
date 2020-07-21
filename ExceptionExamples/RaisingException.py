try:
    a=10;
    if a<18:
        raise ValueError();
    else:
        print("this is a valid age.")
except ValueError:
    print("this value is not correct...please give valid value")

