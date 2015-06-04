'''
Created on May 25, 2015

@author: da_chen
'''
N,T=input().split()
print(N,T)
length_list=[]
length_list=input().split()
s=[]
for j in range(int(T)):
    a,b=input().split()
    a=int(a)
    b=int(b)
    s.append(min(length_list[a:b+1]))
for k in range(len(s)):
    print(s[k])
    