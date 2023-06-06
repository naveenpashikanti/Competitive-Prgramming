'''
You are given a positive integer ‘N’. Your task is to print all prime numbers less than or equal to N.

Sample Input 1 :
7
Sample Output 1 :
2 3 5 7
'''

import sys
import math
sys.setrecursionlimit(10**7)


def primeNumbersTillN(n):
    # Write your code here
    mask = [True]*(n+1)

    for i in range(2, int(math.sqrt(n))+1):
        if mask[i] :
            for j in range(i*i, n+1, i):
                mask[j] = False
    
    ans = []
    for i in range(2, n+1):
        if mask[i]:
            ans.append(i)
        
    return ans
