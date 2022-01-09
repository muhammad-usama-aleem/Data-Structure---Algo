'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1

'''

def maxSubArray(nums):
    for i in range(1, len(nums)):
        print('pre', nums[i-1], 'cur', nums[i])
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
            print('inside', nums[i])
    return max(nums)
  

'''
to understand use this result iteration by iteration
HINT: we are checking if the previous number in the array is greater than 0, if it is then we we (update)add that number in the current number 



pre -2 cur 1
pre 1 cur -3
inside -2
pre -2 cur 4
pre 4 cur -1
inside 3
pre 3 cur 2
inside 5
pre 5 cur 1
inside 6
pre 6 cur -5
inside 1
pre 1 cur 4
inside 5

'''
