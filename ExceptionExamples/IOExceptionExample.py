try:
    with open("D://sus.txt", "r") as f:
        print(f.read());
except IOError:
    print("file not found at the directory..")
else:
    print("file opened successfully")
    f.close()