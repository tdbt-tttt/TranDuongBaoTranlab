# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:55:17 2024

@author: TranDuongBaoTran
"""
import math
a=int(input("Nhập vào số nguyên a: "))
b=int(input("Nhập vào số nguyên b: "))
gt1=a+b
gt2=a**(1/3)+b**(1/3)
gt3=(a*b)**(1/3)
gt4=(a**(1/3)+b**(1/3))**2
A=((gt1/gt2)-gt3)/(gt4)
print("Vậy kết quả của biểu thức là: ",round(A,2))

