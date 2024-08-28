# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:49:09 2024

@author: TranDuongBaoTran
"""
a = int(input("Nhập vào số nguyên a:"))
b = int(input("Nhập vào số nguyên b:"))
c = int(input("Nhập váo số nguyên c:"))
so_lon_nhat = a
if b > so_lon_nhat:
    so_lon_nhat = b
if c > so_lon_nhat:
    so_lon_nhat = c
print("Số lớn nhất là:", so_lon_nhat)    
