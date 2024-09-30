class dagiac:
    def __init__(self,dai,rong):
        self.dai = dai
        self.rong = rong
        
    def nhaptt(self):
        self.dai = int(input('nhập chiều dài của hình: '))
        self.rong = int(input('nhập chiều rộng của hình: '))
class hbh(dagiac):
    def __init__(self,dai,rong,chieucao):
        super().__init__(dai,rong)
        self.chieucao= chieucao
    def nhaptt(self):
        self.chieucao = int(input('nhập chiều cao của hbh:'))
        super().nhaptt()
    def chuvi(self):
        return (self.dai +self.rong)*2
    def dientich(self):
        return self.rong * self.chieucao
    def display(self):
        print('chu vi của hình bh là:',self.chuvi())
        print('diện tích của hình bh là: ',self.dientich())
class hcn(hbh):
    def __init__(self, dai, rong, chieucao):
        super().__init__(dai, rong, chieucao)
    def dientich(self):
        return self.dai*self.rong
    def display(self):
        print('chu vi hình cn là:',self.chuvi())
        print('diện tích hình cn là: ',self.dientich())
        super().display()
class hv(hcn):
    def __init__(self, dai, rong, chieucao,canh):
        super().__init__(dai, rong, chieucao)
        self.canh = canh
    def nhaptt(self):
        self.canh = int(input('nhập cạnh hình vuông: '))
        super().nhaptt()
    def chuvi(self):
        return self.canh*4
    def dientich(self):
        return self.canh*self.canh
    def display(self):
        print('chu vi hình vuông là: ',self.chuvi())
        print('diện tích hình vuông là: ',self.dientich())
        super().display()
        
        
run = hv(0,0,0,0)
run.nhaptt()
run.display()
