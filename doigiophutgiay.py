# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:48:32 2024

@author: TranDuongBaoTran
"""

gio=int(input("Nhập giờ: "))
phut=int(input("Nhập phút: "))
giay=int(input("Nhập giây: "))
tong_giay=gio*3600+phut*60+giay
print("Tổng giây tính được là:",tong_giay)
