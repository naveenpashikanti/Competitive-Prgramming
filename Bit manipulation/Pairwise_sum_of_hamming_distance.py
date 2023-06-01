'''
Hamming Distance for two given integers 'A' and 'B' is 
defined as the minimum number of bits that needs to be toggled 
to make both the integers equal.

For example:
Consider A=4 and B=7
Binary representation of 4 = 100
Binary representation of 7 = 111
For the given example, if we flip the values of the last two least 
significant bits of A to 1 then A will become 7. As we can change the 
value of A to B by 2 flips. Therefore the Hamming Distance, in this case, is 2.

Sample Input 1:
2
3
4 1 3
2
2 2
Sample Output 1:
12
0
Explanation of sample input 1:
For the first test case:
All the 9 possible pairs of array elements are (4,4), (4,1), 
(4,3), (1,4), (1,1), (1,3), (3,4), (3,1), (3,3)
1) (4,4) => Hamming Distance = 0
2) (4,1) => Hamming Distance = 2
3) (4,3) => Hamming Distance = 3 
4) (1,4) => Hamming Distance = 2
5) (1,1) => Hamming Distance = 0
6) (1,3) => Hamming Distance = 1
7) (3,4) => Hamming Distance = 3
8) (3,1) => Hamming Distance = 1
9) (3,3) => Hamming Distance = 0
The sum of all the above values is 12. Therefore, the answer is 12 in this case.

For the second test case:
As all the elements of the array are equal, the hamming distance is 0 for every pair of 
array elements. Therefore the overall sum of Hamming distance is 0 in this case.
'''

# This is also a tricky question. The time complexity is like permutation b/w the array elements.
# Apply brute force, it won't work. We've to see the trend of number of fluip flops in a corrosponding bit position
# in a digit each time in a loop of 30 bits iterate over all elements and check the number of xeros, ones multiply both and 2 that's it

def sumOfHammingDistance(arr, n):
    # Write your code here.
    # count = 0
    # for i in range(n):
    #     for j in range(n):
    #         res = arr[i] ^ arr[j]
    #         filter = 1
    #         while(res):
    #             count += res & filter
    #             res >> 1

    # print(count)

    count = 0
    filter = 1

    for i in range(30):
        zeros, ones = 0, 0

        for elem in arr:
            if elem & filter == 0:
                zeros += 1

            else:
                ones += 1

        count += zeros*ones*2
        filter = filter<<1

    return count

