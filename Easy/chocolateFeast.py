'''
Created on May 29, 2015

@author: da_chen
'''
import math
T = int(input())

for i in range(T):
    N,C,M = str(input()).split()
    N = int(N)
    C = int(C)
    M = int(M)
    chocolate_afford = math.floor(N/C)  
    chocolate_bonus = math.floor(chocolate_afford  / M)
    chocolate_remained=chocolate_afford-chocolate_bonus*M
    chocolate_bonus2=math.floor((chocolate_remained+chocolate_bonus)/M)
    chocolate = chocolate_afford + chocolate_bonus + chocolate_bonus2
    print (chocolate)
