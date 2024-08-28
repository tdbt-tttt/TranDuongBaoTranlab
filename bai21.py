# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:32:35 2024

@author: TranDuongBaoTran 
"""
S=int(input("Nhập vào số bất kì: "))
so_chuoi={0:"Không",1:"Một",2:"Hai",3:"Ba",4:"Bốn",5:"Năm",6:"Sáu",
          7:"Bảy",8:"Tám", 9:"Chín"}
if 0<=S<=9 :
    print(so_chuoi[S])
else:
    print("Không đọc được")
