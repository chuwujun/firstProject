#! /usr/bin/env python3

import os
import sys


def get_true_salary(salary):
    wuxianyijin=salary*0.165
    tax=salary-wuxianyijin-5000
    result=0
    
    if tax<=3000:
        result=tax*0.03
    elif tax>3000 and tax<=12000:
        result=tax*0.1-210
    elif tax>12000 and tax<=25000:
        result=tax*0.2-1410
    elif tax>25000 and tax<=35000:
        result=tax*0.25-2660
    elif tax>35000 and tax<=55000:
        result=tax*0.3-4410
    elif tax>55000 and tax<=80000:
        result=tax*0.35-7160
    elif tax>80000:
        result=tax*0.45-15160
    
    if salary<=5000:
        result=0
    
    true_salary=salary-wuxianyijin-result
    true_salary=format('%.2f' %(true_salary))
    return true_salary

try:
    for arg in sys.argv[1:]:
        id_one=arg.split(":")[0]
        salary=int(arg.split(":")[1])
        true_salary=get_true_salary(salary)
        print(id_one+":"+str(true_salary))
except:
    print("Parameter Error")

