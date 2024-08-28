# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:39:10 2024

@author: TranDuongBaoTran
"""
a = float(input("Nhập hệ số a="))
b = float(input("Nhập hệ số b="))
if a == 0 and b == 0:
    print("Phương trình có vô nghiệm.")
elif a==0 and b !=0:
    print("Phương trình vô số nghiệm")
else:
     print("Phương trình có nghiệm x=",-b/a)
   

