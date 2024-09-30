class hcn:
    def __init__(self,dai,rong):
        self.dai = dai
        self.rong = rong
    def chuvi(self):
        return (self.dai+self.rong)*2
    def dientich(self):
        return self.dai*self.rong
    def nhapthongtin(self):
        self.dai=int(input('nhap chieu dai: '))
        self.rong = int(input('nhap chieu rong: '))
    def display(self):
        print('chieu dai la',self.dai)
        print('chieu rong la',self.rong)
        print('chu vi la',self.chuvi())
        print('dien tich la',self.dientich())

run = hcn(0,0)
run.nhapthongtin()
run.display()