# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:37:11 2024

@author: TranDuongBaoTran
"""
gio = int(input("Nhập giờ:"))
phut = int(input("Nhập phút:"))
giay = int(input("Nhập giây:"))
def kiem_tra_thoi_gian(gio, phut, giay):
    if (0 <= gio < 24) and (0 <= phut < 60) and (0 <= giay < 60):
        return"Thời gian hợp lệ."
    else:
        return"Thời gian không hợp lệ."
ket_qua = kiem_tra_thoi_gian(gio, phut, giay)
print("Kết quả là", ket_qua)
        
