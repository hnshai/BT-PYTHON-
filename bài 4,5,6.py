class Stack:
    def __init__(self,soluong,value):
        self.data = []
        self.soluong = soluong
        self.phantu = 0
        self.stackcount = 0
        self.value = value
    def nhapfloat(self):
        self.value = float(input('nhập phần tử float:'))

    def push(self):
            if self.isfull():
                print('ngăn xếp đã đầy')
                return None
            else:
                self.data.append(self.value)
                self.phantu+=1
                self.stackcount+=1
            
        
    def __del__(self):
        print('mảng đã được hủy')
    def isempty(self):
        return self.phantu == -1
         
    def isfull(self):
        return self.phantu==self.soluong
    def count(self):
        print('số lượng phần tử trong stack là',self.stackcount)
    def display(self):
        print('so pha tu trong mang la',self.data)

run = Stack(soluong=10,value=1)
run.nhapfloat()
run.push()

run.display()
print(run.isempty())
print(run.isfull())
run.count()