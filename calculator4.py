#! /usr/bin/env python3
#coding=utf-8

import sys
import getopt
import csv

#命令行参数类
class Args(object):

    def __init__(self):
        self.args=sys.argv[1:]


#配置文件类
class Config(object):

    def __init__(self):
        self.config=self._read_config()

    def _read_config(self):
        config={}

#用户数据类
class UserData(object):

    def __init__(self):
        self.userdata = self._read_users_data()

    def _read_users_data(self):
        userdata=[]

#税后工资计算类
class IncomeTaxCalculator(object):

    def calc_for_all_userdata(self):
        pass

    def export(self,default='csv'):
        result=self.calc_for_all_userdata(self)
        with open("txt") as f:
            writer=csv.writer(f)
            writer.writerows(result)


#用户数据类
    class UserData(object):

        def __init__(self):
            self.userdata = self._read_users_data()

        def _read_users_data(self):
            userdata=[]

    #税后工资计算类
    class IncomeTaxCalculator(object):

        def calc_for_all_userdata(self):
            pass

        def export(self,default='csv'):
            result=self.calc_for_all_userdata(self)
            with open("txt") as f:
                writer=csv.writer(f)
                writer.writerows(result)

if __name__ == '__main__':
    pass


