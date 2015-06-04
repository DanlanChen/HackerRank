'''
Created on May 21, 2015

@author: da_chen
'''
def solveMeSecond(a,b):
    return a+b
n=int(input())
for i in range(0,n):
    a,b=input().split()
    a,b=int(a),int(b)
    res =solveMeSecond(a, b)
    print(res)