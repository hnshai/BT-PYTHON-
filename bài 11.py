import math

class tamgiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def kiem_tra_hop_le(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def tinh_chu_vi(self):
        if self.kiem_tra_hop_le():
            return self.a + self.b + self.c
        else:
            return "Không phải là tam giác"

    def tinh_dien_tich(self):
        if self.kiem_tra_hop_le():
            p = self.tinh_chu_vi() / 2
            return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        else:
            return "Không phải là tam giác"

class tamgiacvuong(tamgiac):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        if self.kiem_tra_hop_le() and (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
            print("Đây là tam giác vuông")
        else:
            print("Không phải tam giác vuông")

class tamgiaccan(tamgiac):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        if self.kiem_tra_hop_le() and (a == b or a == c or b == c):
            print("Đây là tam giác cân")
        else:
            print("Không phải tam giác cân")

class tamgiacdeu(tamgiaccan):
    def __init__(self, canh):
        super().__init__(canh, canh, canh)
        if self.kiem_tra_hop_le():
            print("Đây là tam giác đều")
        else:
            print("Không phải tam giác đều")

# Ví dụ sử dụng:
tg1 = tamgiac(3, 4, 5)
print("Chu vi:", tg1.tinh_chu_vi())
print("Diện tích:", tg1.tinh_dien_tich())

tg2 = tamgiacvuong(3, 4, 5)
tg3 = tamgiaccan(2, 2, 3)
tg4 = tamgiacdeu(5)