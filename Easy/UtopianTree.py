'''
Created on May 21, 2015

@author: da_chen
'''
T = int(input())
for i in range(0,T):
    N =int(input())
    h=1
    for j in range(1,N+1):
        if j%2==0:
            h=h+1
        else:
            h=2*h
    print (h)
