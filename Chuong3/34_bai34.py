t=float(input())
l=float(input())
h=float(input())
dtb=(t*2+l*3+h)/6
if dtb<3:xl='Kem'
elif dtb<5:xl='Yeu'
elif dtb<6:xl='Trung binh'
elif dtb<7:xl='Trung binh kha'
elif dtb<8:xl='Kha'
elif dtb<9:xl='Gioi'
else:xl='Xuat sac'
print(xl)