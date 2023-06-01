'''
You are given two integers N and i. You need to make ith bit of binary 
representation of N to 0 and return the updated N.
Counting of bits start from 0 from right to left.

Sample Input 1 :
1
7 2
Sample Output 1 :
3
'''

t = int(input())
for _ in range(t):
    n, i = map(int, input().split())
    print(n&(~(1<<i)))

