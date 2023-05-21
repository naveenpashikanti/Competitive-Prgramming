'''Write a recursive function 
that returns the sum of 
the digits of a given integer.

Sample Input 1 : 12345

Sample Output 1 : 15

'''

def sumDigits(n):
    if n == 0:
        return 0
    
    return n%10 + sumDigits(n//10)


## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())

print(sumDigits(n))