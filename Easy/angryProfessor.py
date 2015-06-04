'''
Created on May 27, 2015

@author: da_chen
'''
T=int(input())
aptitude=[]
for i in range(T):
    N,K=list(map(int,input().split()))
    time_li=input().split()
    time_li=list(map(int,time_li))
    count=0
    for j in range(N):
        if time_li[j]<=0:
            count+=1
    if count>=K:
        aptitude.append("no")
    else:
        aptitude.append("yes")
for k in range(len(aptitude)):
    print (aptitude[k])     
