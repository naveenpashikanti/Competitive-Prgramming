'''You are given an array 'nums' consisting of first N positive integers. 
But from the N integers, one of the integers occurs twice in the array, and one of 
the integers is missing. You need to determine the repeating and the missing integer.

Example:
Let the array be [1, 2, 3, 4, 4, 5]. In the given array ‘4’ occurs twice and 
the number ‘6’ is missing.'''

def findRepeatingAndMissingNumbers(nums):
    # Write your Code here.
    xorr = 0
    i = 1
    for num in nums:
        xorr ^= num
        xorr ^= i
        i += 1

    set_bit = xorr & ~(xorr-1)

    x_set, y_not_set = 0, 0

    i = 1
    for num in nums:
        if num & set_bit:
            x_set ^= num

        if not(num & set_bit):
            y_not_set ^= num        

        if i & set_bit:
            x_set ^= i

        if not(i & set_bit):
            y_not_set ^= i

        i += 1

    for num in nums:
        if x_set == num:
            return x_set, y_not_set

    
    return y_not_set, x_set