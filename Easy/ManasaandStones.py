'''
Created on Jun 2, 2015

@author: da_chen
'''
T=int(input())
for i in range(T):
    final=[]
    n=int(input())
    a=int(input())
    b=int(input())
    for j in range(n):
        fi=a*j+(n-1-j)*b
        final.append(fi)
    final=sorted(final)
   
for lis in output:
    for i in lis:
        print(i ,end=" ")
    print("\t")
   
