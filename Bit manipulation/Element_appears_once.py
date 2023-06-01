'''
Element that Appears Once
Send Feedback
You are given an arbitrary array ‘arr’ consisting of 
N non-negative integers, where every element appears thrice except one. 
You need to find the element that appears only once.

Sample Input 1:
1
4
1 2 1 1
Sample Output 1:
2

'''

def elementThatAppearsOnce(arr):
    # Write your code here
    # Return the integer which appears only once.
    a = [0]*31
    for elem in arr:
        bin_r = bin(elem)[2:]
        for ind, char in enumerate(bin_r[::-1]):
            a[ind] += int(char)

    unique = 0
    for ind, val in enumerate(a):
        if val%3 :
            unique += 2**ind

    return unique

