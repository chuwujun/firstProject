# -*- coding: utf-8 -*-

import re
from datetime import datetime

def open_parser(filename):
    with open(filename) as logfile:
        pattern=(r''
                 r'(\d+.\d+.\d+.\d+)\s-\s-\s'
                 r'\[(.+)\]\s'
                 r'"GET\s(.+)\s\w+/.+"\s'
                 r'(\d+)\s'
                 r'(\d+)\s'
                 r'"(.+)"\s'
                 r'"(.+)"'
                 )
        parsers=re.findall(pattern,logfile.read())
    return parsers

def main():
    logs=open_parser('/home/shiyanlou/Code/nginx.log')
    #print(logs[1])
    list20170111=[]
    for item in logs:
        if item[1][:11]=="11/Jan/2017":
            list20170111.append(item)
    #for item in list20170111:
    #    print(item)
    dict1={}
    count=0
    for item in list20170111:
        if item[0] not in dict1:
            dict1[item[0]]=1
        else:
            dict1[item[0]]+=1
    ip_20170111=""
    max_20170111=0
    for key,value in dict1.items():
        if value>max_20170111:
            max_20170111=value
            ip_20170111=key
    ip_dict={ip_20170111:max_20170111}
    #print(ip_dict)

    list_404=[]
    for item in logs:
        if item[3] == '404':
            list_404.append(item)
    dict2={}
    count=0
    for item in list_404:
        if item[2] not in dict2:
            dict2[item[2]]=1
        else:
            dict2[item[2]]+=1
    url=""
    max_404=0
    for key,value in dict2.items():
        if value>max_404:
            url,max_404=key,value
    url_dict={url:max_404}
    return ip_dict,url_dict

if __name__ == '__main__':
    ip_dict,url_dict=main()
    print(ip_dict,url_dict)
