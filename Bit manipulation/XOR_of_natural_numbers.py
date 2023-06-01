'''
You are given an integer N and asked to find the Xor of first N natural numbers.
'''

# This is a very tricky question. we've to utilise the property of natural numbers repeating trend in xor 
# First think about brute force then check why it won't work in real situations, the time complexity crosses
# very fastly. So, if ypu keenly observe the xor of consecutve 4 numbers have repeating trend

t = int(input())
for _ in range(t):
    n = int(input())
    if(n%4 == 1):
        print(1)
    elif(n%4 == 2):
        print(n+1)
    elif(n%4 == 3):
        print(0)
    else:
        print(n)    
