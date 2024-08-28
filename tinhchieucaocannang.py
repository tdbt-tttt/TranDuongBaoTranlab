# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:16:18 2024

@author: TranDuongBaoTran
"""
can_nang = float(input("Nhập cân nặng(kg)"))
chieu_cao = float(input("Nhập chiều cao(m)"))
bmi = can_nang / (chieu_cao ** 2)
print("Chỉ số bmi của bạn là:",bmi)
if bmi < 18.5:
    print("Bạn bị gầy")
elif 18.5 <= bmi < 24.9:
    print("Bạn có trọng lượng bình thường ")
elif 25 <= bmi < 29.9:
    print("Bạn bị thừa cân ")
