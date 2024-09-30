class TS:
    def __init__(self,name,toan,ly,hoa):
        self.name = name
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
    def tongdiem(self):
        return self.toan +self.ly+self.hoa
    def display(self):
      if self.tongdiem() >20: 
        print('tên sinh vien là:', self.name)
        print('điểm toán của  sinh vien la:', self.toan)
        print('điểm lý của  sinh vien la:',self.ly)
        print('điểm hóa của  sinh vien la: ',self.hoa)
        print('điểm tổng của sinh viên là:',self.tongdiem())
