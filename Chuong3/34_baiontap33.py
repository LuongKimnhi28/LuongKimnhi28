tieuthu=int(input('Tieu thu='))
if 1<= tieuthu <=100:
    gia=550
elif tieuthu <=150:
    gia=750*(tieuthu-100)+100*550
elif tieuthu <200:
    gia=100*550+50*750+(tieuthu-150)*950
else: gia=100*550+50*750+50*950+(tieuthu-200)*1350
print('Phai tra=',round(gia*1.1,1),sep='')