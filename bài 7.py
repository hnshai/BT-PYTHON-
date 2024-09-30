class Date:
    def __init__(self,ngay,thang,nam):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam
    def tgian(self):
        self.ngay = int(input('nhập ngày: '))
        self.thang = int(input('nhập tháng: '))
        self.nam = int(input('nhập năm: '))
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
    
    def next(self):
        self.ngay+=1
        if self.ngay>31:
            self.ngay = 1
            self.thang+=1
            if self.thang>12:
                self.thang = 1
                self.nam+=1
        return self.ngay,self.thang,self.nam
    def display(self):
        print('ngày tháng năm là: ',self.ngay,self.thang,self.nam)
        print('next là: ',self.next())
             
    def tinhnam(self):
        return self.nam//400==0 or self.nam%4 == 0 and self.nam%100 !=0

run = Date(0,0,0)
run.tgian()

run.display()
