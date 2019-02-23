#! /usr/bin/env python3
import sys
import csv
import getopt

cfg_file=""
input_file=""
output_file=""

orgs,args=getopt.getopt(sys.argv[1:],'c:d:o:')
for param,filename in orgs:
    if param=='-c':
        cfg_file=filename
    if param=='-d':
        input_file=filename
    if param=='-o':
        output_file=filename
#print(cfg_file,input_file,output_file)


#get config file
with open(cfg_file,'rb') as f:
    cfg_list=f.readlines()
cfg_num_list=[float(x.split('=')[1].strip()) for x in cfg_list if x.find('=') !=-1 ]
#for one in cfg_num_list:
#    print(one)
tax_min=cfg_num_list[0]
tax_max=cfg_num_list[1]
tax_rate=0
for i in range(2,8):
    tax_rate+=cfg_num_list[i]
def get_info(id,salary):
    sala=salary
    salary=float(salary)
    wuxianyijin=float(salary)*float(tax_rate)
    if salary<float(tax_min):
        wuxianyijin=float(tax_min)*float(tax_rate)
    if salary>float(tax_max):
        wuxianyijin=float(tax_max)*float(tax_rate)
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
    wuxianyijin=format('%.2f' %(wuxianyijin))
    result=format('%.2f' %(result))
    return (id,sala,wuxianyijin,result,true_salary)
#get user.csv
with open(input_file,'rb') as f:
    cf=csv.reader(f)
    user_list=list(cf)
for one in user_list:
    id=one[0]
    salary=one[1]
    returns=get_info(id,salary)
    f=open(output_file,'a')
    f.write(str(returns[0])+','+str(returns[1])+','+str(returns[2])+','+str(returns[3])+','+str(returns[4]))
    f.write("\n")
    f.close()

