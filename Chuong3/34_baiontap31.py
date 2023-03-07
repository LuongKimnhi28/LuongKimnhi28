a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a>b and a>c:
    SLN=a
elif b>a and b>c:
    SLN=b
else: SLN=c
if a<b and a<c:
    SBN=a
elif b<a and b<c:
    SBN=b
else: SBN=c
print('SLN=',SLN,sep='')
print('SBN=',SBN,sep='')