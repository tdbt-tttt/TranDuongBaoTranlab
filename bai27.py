# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:40:32 2024

@author: TranDuongBaoTran 
"""
#Hình chữ nhật
a=int(input("Nhập vào cạnh a: "))
b=int(input("Nhập vào cạnh b: "))
chu_vi = (a + b) * 2
print("Chu vi hình chữ nhật là: ",chu_vi)
dien_tich = a * b
print("Diện tích hình chữ nhật là: ",dien_tich)

#Hình vuông
a=int(input("Nhập vào độ dài cạnh a: "))
chu_vi = a * 4
print("Chu vi hình vuông là: ",chu_vi)
dien_tich = a * a
print("Diện tích hình vuông là: ",dien_tich)

#Hình tròn
import math
R=int(input("Nhập vào bán kính của hình : "))
chu_vi = 2 * math.pi * R
print("Chu vi hình tròn là : ",chu_vi)
dien_tich = math.pi * R ** 2
print("Diện tích hình tròn là: ",dien_tich)
