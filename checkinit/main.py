import os
import sys
import re

#get file name list
def get_file_list(dirpath):
    file_list=[]
    all_list=os.listdir(dirpath)
    for i in range(0,len(all_list)):
        path=os.path.join(dirpath,all_list[i])
        if os.path.isfile(path):
            file_list.append(path)
        else:
            file_list.extend(get_file_list(path))
    return file_list


file_type=['.c','.h']
normal_type=['int','float','double','char','long','short']
current_path=os.path.abspath(sys.argv[0])
dirlist=current_path.split(os.sep)
code_dir=(os.sep).join(dirlist[0:-1])+os.sep+'Code'
file_list=get_file_list(code_dir)
clear_list=[]
for one in file_list:
    if ''.join(one[-2:]) not in file_type:
        clear_list.append(one)
for clear in clear_list:
    if clear in file_list:
        file_list.remove(clear)
for file in file_list:
    line_num=0
    file_content=[]
    f=open(file,'r')
    file_content=f.readlines()
    f.close()
    for i in range(0,len(file_content)):
        line=file_content[i].replace('\n','')
        line=line.strip()
        line_num=line_num+1
        #print line
        for one_type in normal_type:
            #exclude function
            if re.match(one_type,line)  and line.find('(')==-1 :
                if line.find('=')==-1:
                    print "["+one_type+" error] line_num is :"+str(line_num)+" in "+file
