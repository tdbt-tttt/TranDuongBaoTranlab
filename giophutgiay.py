# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:51:50 2024

@author: TranDuongBaoTran 
"""
gio = int(input("Nhập giờ:"))
phut = int(input("Nhập phút"))
giay = int(input("Nhập giây"))
tong_giay = gio * 3600 + phut * 60 + giay
print("Tổng số giây là:", tong_giay)
