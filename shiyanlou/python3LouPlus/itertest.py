#! /usr/bin/env python3

testlist=['Linux','Java','Python','DevOps','Go']

it=iter(testlist)
print("Loop Start...")

while True:
    try:
        course=next(it)
        print(course)
    except StopIteration:
#raise StopIteration
        break
    except OverflowError:
        print("Loop End")
print("Loop End")
