# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:45:39 2024

@author: TranDuongBaoTran
"""
chu_cai = input("Nhập vào một chữ cái:")
chu_cai_nhap = input("Nhập một chữ cái:")
def doi_chu_cai(chu_cai):
 if chu_cai.islower() :
     return chu_cai.upper()
 elif chu_cai.isupper():
     return chu_cai.lower()
 else:
     return "Vui lòng nhập một chữ cái"
 ket_qua = doi_chu_cai(chu_cai_nhap)
 print("Chữ cái sau khi đổi là:", ket_qua)