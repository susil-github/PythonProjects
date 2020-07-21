temp=[10,-20,-289,100]
def centToFarhenhite(c):
    if c<-273.15:
        return "that temp does not make sense";
    else:
        f=c*9/5+32;
        return f;
for t in temp:
    print(centToFarhenhite(t));