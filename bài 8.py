class employee:
    def __init__(self,name=1,ngay=1,thang=1,nam=1000):
            self.name = name
            self.ngay = ngay
            self.thang = thang
            self.nam = nam
    def nhaptt(self):
            self.name = str(input('nhập họ và tên: '))
            self.ngay = int(input('nhập ngày sinh: '))
            self.thang = int(input('nhập tháng sinh: '))
            self.nam = int(input('nhập năm sinh: '))
            if self.thang in [1,3,5,7,8,10,12]:
                if 0<self.ngay<=31:
                    return self.ngay
                else: print('vui lòng nhập lại ngày ')
            elif self.thang in [4,6,9,11]:
                if 0<self.ngay<=30:
                    return self.ngay
                else:
                    print('vui lòng nhập lại ngày')
            else: 
                if self.tinhnam():
                    if 0<self.ngay<=29:
                        return self.ngay
                    else:
                        print('vui lòng nhập lại ngày')
                else:
                    if 0<self.ngay<=28:
                        return self.ngay
                    else:
                        print('vui lòng nhập lại ngày')
            if 0<self.thang<=12:
                return self.thang
            else: print('vui lòng nhập lại tháng')
            if 1990<self.nam<=2025:
                return self.nam
            else: print('vui lòng nhập lại năm')
    def tinhnam(self):
        return self.nam//400==0 or self.nam%4 == 0 and self.nam%100 !=0

    

    def display(self):
        print('ngày tháng năm sinh là: ',self.ngay,self.thang,self.nam)
        print('họ và tên là: ',self.name)    

run = employee()
run.nhaptt()
run.display()