'''Segmented Sieve Problem
In this problem you have to print all primes from given interval.

Sample Input:
2
2 10
3 7
Sample Output:
2 3 5 7
3 5 7 
'''

import math
t = int(input())

for _ in range(t):
    l, r = map(int, input().split())

    primes = [True]*(r-l+1)
    primes_upto_r = [True]*(math.ceil(math.sqrt(r)))

    for i in range(2, math.ceil(math.sqrt(len(primes_upto_r))) ):

        if primes_upto_r[i] == True:

            for j in range(2*i, len(primes_upto_r), i):
                primes_upto_r[j] = False

    primes_upto_r_found = []

    for i in range(2, len(primes_upto_r)):
        if(primes_upto_r[i]):
            primes_upto_r_found.append(i)

    for prime in primes_upto_r_found:

        if l % prime:
            first_divided = (l//prime)* prime + prime
        
        else:
            first_divided = l+i

        for i in range(first_divided, r, prime):
            if (i%prime) == 0:
                primes[i-l] = False

    final_list = []
    for elem in primes:
        if elem:
            final_list.append(elem+l)

    print(final_list)