m1=int(input('M1='))
m2=int(input('M2='))
m3=int(input('M3='))
s=int(input('S='))
if s<=100:
    gia=s*m1
elif 101<=s<=150:
    gia=(s-100)*m2+100*m1
else: gia=100*m1+50*m2+(s-150)*m3
print('Phai tra=',gia,sep='')