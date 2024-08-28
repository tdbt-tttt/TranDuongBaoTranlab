# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:21:26 2024

@author: TranDuongBaoTran
"""

so_xe = input("Nhập vào số xe của bạn:")
tong = sum(int(chu_so) for (chu_so) in (so_xe))
hang_chuc = tong // 10
hang_don_vi = tong % 10
so_nut = hang_chuc + hang_don_vi
print("Số xe của bạn được số nút: ",so_nut)