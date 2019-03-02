#! /usr/bin/env python3

f=open('shiyanlou.txt','r')
lista=f.readlines()
f.close

f=open('shiyanlou_copy.txt','a')
for i,a in enumerate(lista):
    f.write(str(i+1)+" "+a)
f.close()
