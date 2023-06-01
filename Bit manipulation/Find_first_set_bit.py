'''
You are given an integer N. You need to return an integer M, in which only one bit is set 
which at the position of a lowest set bit of N (from right to left).

Sample Input 1 :
1
7

Sample Output 1 :
1
'''

t = int(input())

for _ in range(t):
    n = int(input())

    filter_ = 1
    a = n
    flag = 0

    while(a > 0):
        if n & filter_:
            break

        filter_ = filter_ <<1
        a = a>>1

    print(filter_)