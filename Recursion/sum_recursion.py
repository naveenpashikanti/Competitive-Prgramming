'''Given an array of length N, 
you need to find and return 
the sum of all elements of the array.
Do this recursively.'''

def sumArray(arr):
    # Please add your code here
    if arr == []:
        return 0

    return res + sumArray(arr[1:])


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))

