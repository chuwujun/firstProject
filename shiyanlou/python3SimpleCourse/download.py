#! /usr/bin/env python3

import os
import os.path
import requests

def download(url):
    req=requests.get(url)
    if req.status_code==404:
        print('not such file found at %s' %(url))
        return
    filename=url.split('/')[-1]
    with open(filename,'wb')as fobj:
        fobj.write(req.content)
    print("download over")

url=input("enter a url")
download(url)
