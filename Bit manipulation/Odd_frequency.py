'''
You are given an array of size N with all elements 
with even frequency except one and you are supposed to find this element.
'''

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    xorr = 0
    for elem in a:
        xorr = xorr ^ elem
    print(xorr)