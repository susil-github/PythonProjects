class Bank:
    def getroi(self):
        return 10

class SBI(Bank):
    def getroi(self):
        return 20

class ICICI(Bank):
    def getroi(self):
        return 30

b= Bank()
s=SBI()
i=ICICI()
print("bank interest is ",b.getroi())
print("SBI interest is ",s.getroi())
print("ICICI interest is ",i.getroi())
