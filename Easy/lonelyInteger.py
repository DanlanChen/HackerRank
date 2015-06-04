'''
Created on May 26, 2015

@author: da_chen
'''
#!/usr/bin/py
# Head ends here
import operator
import functools
def lonelyinteger(b):
    N=int(input())
    s=[]
    s=input().split()
    s=map(int,s)
    answer=functools.reduce(operator.xor, s)
    print (answer)
lonelyinteger()