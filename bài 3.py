class PS:
    def __init__(self,tuso,mauso):
        self.tuso = tuso
        self.mauso = mauso
    def nhapps(self):
        self.tuso=int(input('nhap tu so: '))
        self.mauso=int(input('nhap mau so: '))
        if self.mauso ==0:
            print('Mau so phai khac 0')
            return False
        else:
            return True
    def inthongtin(self):
        print('phân số là: ',self.tuso/self.mauso)        

n = PS(0,0)
if n.nhapps():
    n.inthongtin()
else:
    print('phân số không hợp lệ')