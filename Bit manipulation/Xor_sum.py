'''
You are given two arrays, ‘arr1’ of size 'N' and ‘arr2’ of size 'M'. 
You need to create an array of bitwise AND of all the possible pairs between 
the elements of both arrays, and your task is to find the XOR sum of the array. 
The XOR sum of an array is equal to the XOR of all elements of the array.

You are given an ‘arr1’ = [3, 2, 8] and ‘arr2’ = [1, 4, 3], therefore the AND of all possible 
pairs is [(3 & 1), (3 & 4), (3 & 3), (2 & 1), (2 & 4), (2 & 3), (8 & 1), (8 & 4), (8 & 3)]. 
So the resulting Array will be [1, 0, 3, 0, 0, 2, 0, 0, 0] therefore XOR sum of the result array is 0 . 
Hence the answer is 0.

Sample Input 1:
2
3 3
3 2 8
1 4 3
2 1
4 12
8
Sample Output 1:
0
8
Explanation :
For the first test case, ‘arr1’ = [3, 2, 8] and ‘arr2’ = [1, 4, 3], 
therefore the AND of all possible pairs is [(3 & 1), (3 & 4), (3 & 3), (2 & 1), (2 & 4), (2 & 3), 
(8 & 1), (8 & 4), (8 & 3)]. So the resulting array will be [1, 0, 3, 0, 0, 2, 0, 0, 0] therefore XOR sum of the result array is 0. 
Hence the answer is 0.

For the second test case ‘arr1’ = [4, 12] and ‘arr2’ = [8], therefore the AND of all possible pairs 
is [(4 & 8), (12 & 8)]. So the resulting array will be [0, 8] therefore XOR sum of the result array is 8. 
Hence the answer is 8.

'''

from typing import List

def xorSum(arr1: List[int], arr2: List[int]) -> int:
    # Write your code here

    res = 0
    filter_ = 1

    for i in range(30):
        count_a = 0

        for elem in arr1:
            if elem & filter_:
                count_a += 1

        count_b = 0
        for elem in arr2:
            if elem & filter_:
                count_b += 1

        if (count_a*count_b) % 2:
            res += 2**i

        filter_ = filter_ << 1

    return res