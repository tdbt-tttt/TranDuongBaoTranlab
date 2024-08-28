# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:13:31 2024

@author: TranDuongBaoTran
"""
a = float(input("Nhập hệ số a="))
b = float(input("Nhập hệ số b="))
c = float(input("Nhập hệ số c="))
import math
delta = b**2-4*a*c
if delta < 0:
      print("Phương trình vô nghiệm")
elif delta==0:
      x=-b/(2*a)
      print("Phương trình có nghiệm kép x1 x2",x)
elif delta>0:
      x1 = ( -b + math.sqrt(delta)) / (2*a)
      x2 = ( -b - math.sqrt(delta)) / (2*a)
      print("Phương trình có hai nghiệm phân biệt x1= x2=",x1,x2)
  

      
      
      
