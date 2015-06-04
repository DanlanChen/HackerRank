'''
Created on May 25, 2015

@author: da_chen
'''
import math
N=int(input())
count=[]
for i in range(N):
    s=input()
    le=len(s)
    c=0
    for j in range(math.floor((le-1)/2)+1):
      c+=abs(ord(s[j])-ord(s[le-j-1]))
    count.append(c)
for k in range(len(count)):
    print(count[k])
      