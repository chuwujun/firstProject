#! /usr/bin/env

def infinite_generator(start=0):
    while True:
        yield start
        start+=1


for num in infinite_generator(4):
    print(num,end=' ')
    if(num>20):
        break


