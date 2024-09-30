from Student import TS
DSTS = []
while True:
    print('''
    VUI LÒNG CHỌN CHỨC NĂNG:
          0.thoát
          1.in thông tin
          2.nhập thông tin 
          ''')
    chon = input('Nhập chức năng: ')
    if chon.isdigit():
        chon = int(chon)
        if chon==0:
            break
        elif chon ==1:
            if len(DSTS)==0:print('không có thí sinh nào')
            else:
                for i in DSTS:
                    i.display()
        elif chon==2:
            name = str(input('Nhap ten ts: '))
            toan = float(input('Nhap diem toan: '))
            ly = float(input("Nhap diem ly: "))
            hoa = float(input("Nhap diem hoa: "))
            DSTS.append(TS(name,toan,ly,hoa))
    else:
        print("Vui lòng chọn lại") 