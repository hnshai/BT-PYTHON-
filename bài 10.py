class diem:
    def __init__(self,pi = 3.14):
        self.pi = pi
class tron(diem):
    def __init__(self, pi=3.14, bankinh=0):
        super().__init__(pi)
        self.bankinh = bankinh
    def nhaptt(self):
        self.bankinh = float(input('nhập bán kính đường tròn: '))
    def dientich(self):
        return self.pi *self.bankinh**2
    def display(self):
        print('diện tích hình tròn là: ',self.dientich())
class elip(tron):
    def __init__(self, pi=3.14, bankinh=0,a = 0,b = 0):
        super().__init__(pi, bankinh)
        self.a = a
        self.b = b
    def nhaptt(self):
        self.a = float(input('nhập độ dài bán trục lớn: '))
        self.b = float(input('nhập độ dài bán trục nhỏ: '))
        super().nhaptt()
    def dientich(self):
        return self.pi *self.a *self.b
    def display(self):
        print('diện tích hình elip là',self.dientich())
        super().display()
run = elip()
run.nhaptt()
run.display()