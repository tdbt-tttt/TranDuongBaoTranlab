# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:09:55 2024

@author: TranDuongBaoTran
"""
n = int(input("Nhập số nguyên dương có 2 chữ số:"))
chu_so_1 = n // 10 
chu_so_2 = n % 10 
tong = chu_so_1 + chu_so_2 

if 10 <= n <= 99:
    print("chu_so_1 + chu_so_2: ", tong)
else:
    print("không hợp lệ")
