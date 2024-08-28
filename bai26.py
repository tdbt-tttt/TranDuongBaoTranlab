# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:37:42 2024

@author: TranDuongBaoTran 
"""
#Câu a
a=int(input("Nhập vào hệ số a: "))
b=int(input("Nhập vào hệ số b: "))
c=int(input("Nhập vào  số c: "))
if a > b:
    a,b=b,a
elif a > c:
    a,c=c,a
elif b > c:
    b,c=c,b
print("Các số từ nhỏ đến lớn: ", a,b,c)
    
#Câu b
N=int(input("Nhập vào số nguyên N: "))
digits=[int(d) for d in str(N)]
digits.sort()
ket_qua=int(''.join(map(str,digits)))
print("Kết quả là: ",ket_qua)
