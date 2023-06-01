'''You are given two integers N and i. You need to clear all bits 
from MSB to ith bit (start i from right to left) and return the updated N.
Counting of bits starts from 0 from right to left

Sample Input 1 :
1
15 2
Sample Output 1 :
3
'''

t = int(input())
for _ in range(t):
    n, i = map(int, input().split())
    filter = (1<<i) - 1
    print(n & filter)