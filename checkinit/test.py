import re

with open('aaa','r') as f:
    c=f.read()

d=re.compile(r'struct\s*?(\w*)\s*\{.*?\}\s*([\w,_]*)\s*;',re.S)
print d.findall(c)
#.groups()
#e=re.compile(r'struct\s*([\w,_]*)\s*(\w)*',re.S)
#print e.findall(c)
