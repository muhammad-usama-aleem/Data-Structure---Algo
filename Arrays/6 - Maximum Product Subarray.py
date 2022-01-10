'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

'''


def maxProduct(nums):
    global_max = prev_max = prev_min = nums[0]
    for num in nums[1:]:
        print('Before======', 'prev_max', prev_max, 'prev_min', prev_min, 'global_max', global_max)
        curr_min = min(prev_max*num, prev_min*num, num)
        curr_max = max(prev_max*num, prev_min*num, num)
        global_max= max(global_max, curr_max)
        prev_max = curr_max
        prev_min = curr_min
        print('After======', 'prev_max', prev_max, 'prev_min', prev_min, 'global_max', global_max)
    return global_max
  
  
'''
EXAMPLE: [2,3,-2,4]
Before====== prev_max 2 prev_min 2 global_max 2
After====== prev_max 6 prev_min 3 global_max 6
Before====== prev_max 6 prev_min 3 global_max 6
After====== prev_max -2 prev_min -12 global_max 6
Before====== prev_max -2 prev_min -12 global_max 6
After====== prev_max 4 prev_min -48 global_max 6


'''
