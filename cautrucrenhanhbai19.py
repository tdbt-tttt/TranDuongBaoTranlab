# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:41:35 2024

@author: TranDuongBaoTran
"""
a = int(input("Nhập vào số nguyên a:"))
b = int(input("Nhập vào số nguyên b:"))
c = int(input("Nhập vào số nguyên c:"))
d = int(input("Nhập vào số nguyên d:"))
nho_nhat = a
if b < nho_nhat:
    nho_nhat = b
if c < nho_nhat:
    nho_nhat = c
if d < nho_nhat:
    nho_nhat = d
print("Giá trị nhỏ nhất là:", nho_nhat)    
