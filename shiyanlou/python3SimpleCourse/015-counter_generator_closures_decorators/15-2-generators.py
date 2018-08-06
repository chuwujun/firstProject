#! /usr/bin/env python3

#该例为生成器例子，代码如下
#生成器每次调用，都从上次yield处接着往下进行

def my_generator():
    print("Inside my generate:")
    yield 'a'
    yield 'b'
    yield 'c'

for char in my_generator():
    print(char)



def counter_generator(low,high):
    while low<=high:
        yield low
        low+=1

for i in counter_generator(5,10):
    print(i,end=' ')

