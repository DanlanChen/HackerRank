'''
Created on May 26, 2015

@author: da_chen
'''
N=int(input())
s=input().split()
s=list(map(int,s))
print(s)
count=[]
while len(s)>0:
    minn=min(s)
    count.append(len(s))
    for i in range(len(s)):
        s[i]=s[i]-minn
    s=list(filter(lambda a :a!=0,s))
for j in range(len(count)):
    print(count[j])    