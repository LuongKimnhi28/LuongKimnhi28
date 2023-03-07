ngaynghi=int(input())
if ngaynghi==0:
    xl='Xep loai A'
elif ngaynghi<2:
    xl='Xep loai B'
elif ngaynghi<4:
    xl='Xep loai C'
else:xl='Xep loai D'
print(xl)