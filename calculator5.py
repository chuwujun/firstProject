#! /usr/bin/env python3
#coding=utf-8

import sys
import getopt
import csv
import configparser
import datetime

#命令行参数类
class Args(object):

    def __init__(self):
        self.args=sys.argv[1:]

    def read_files(self):
        org_s,arg_s=getopt.getopt(self.args,'C:c:d:o:')
        for org,filename in org_s:
            if org == '-c':
                config_file=filename
            if org == '-d':
                user_file=filename
            if org == '-o':
                output_file=filename
            if org == '-C':
                city=filename
        return (config_file,user_file,output_file,city)
        


#配置文件类
class Config(object):

    def __init__(self,filename,city):
        self.filename=filename
        self.city=city
        self.config=self._read_config()

    def _read_config(self):
        config={}
        conf=configparser.ConfigParser()
        conf.read(self.filename)
        sections=conf.sections()
        for one in sections:
            if one.lower() == self.city.lower():
                city=one
        config=dict(conf.items(city))
        return config

#用户数据类
class UserData(object):

    def __init__(self,filename):
        self.filename=filename
        self.userdata = self._read_users_data()

    def _read_users_data(self):
        userdata=[]
        f=open(self.filename,'r')
        content=f.readlines()
        f.close()
        for item in content:
            idone,salary=item.split(',')
            salary=salary.replace("\n","")
            userdata.append((idone,salary))
        return userdata

#税后工资计算类
class IncomeTaxCalculator(object):

    def __init__(self,filename,config_dict,user_list):
        self.config=config_dict
        self.user=user_list
        self.filename=filename


    def calc_for_all_userdata(self):
        all_list=[]
        for idone,salary in self.user:
            list_one=[]
            list_one.append(idone)
            list_one.append(salary)
            salary=float(salary)
            +float(self.config['shiye'])+float(self.config['gongshang'])
            +float(self.config['shengyu'])+float(self.config['gongjijin'])
            #print('%.3f' %sums)
            sums=float(self.config['yanglao'])+float(self.config['yiliao'])+float(self.config['shiye'])+float(self.config['gongshang'])+float(self.config['shengyu'])+float(self.config['gongjijin'])
            #print('%.3f' %sums)
            #for _,values in self.config.items():
            #    print(float(values))
            shebao=salary*sums
            if salary<float(self.config['jishul']):
                shebao=float(self.config['jishul'])*sums
            if salary>float(self.config['jishuh']):
                shebao=float(self.config['jishuh'])*sums

            tax=salary-shebao-5000
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
    
            true_salary=salary-shebao-result
            true_salary=format('%.2f' %(true_salary))
            shebao=format('%.2f' %(shebao))
            result=format('%.2f' %(result))
            dates=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            list_one.append(str(shebao))
            list_one.append(str(result))
            list_one.append(str(true_salary))
            list_one.append(str(dates))
            all_list.append(list_one)
        return all_list
        
    def export(self):
        result=self.calc_for_all_userdata()
        with open(self.filename,'w') as f:
            writer=csv.writer(f)
            writer.writerows(result)


if __name__ == '__main__':
    all_arg=Args()
    config_file,user_file,output_file,city=all_arg.read_files()
    
    config=Config(config_file,city)
    config_dict=config.config
    user_list=UserData(user_file).userdata
    
    m=IncomeTaxCalculator(output_file,config_dict,user_list)
    m.export()
