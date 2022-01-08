'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

'''


import math
import numpy as np


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         Solution # 1


        # arr = []
        # mul = []
        # for num, val in enumerate(nums):
        #     arr = nums[:]
        #     del arr[num]
        #     mul.append(math.prod(arr))
        # return (mul)
        
        
#         Solution # 2


#         ans = [1 for _ in nums]
        
#         left = 1
#         right = 1
        
#         for i in range(len(nums)):
#             ans[i] *= left
#             ans[~i] *= right
#             print('left', left, 'right', right, 'before ans', ans)
#             left *= nums[i]
#             right *= nums[~i]
#             print('left', left, 'right', right, 'ans', ans)
        
#         return ans
    
    
    
#         Solution # 3
        mul = [1 for _ in nums]
        temp = 1
        val = 0
        arr = nums[:]
        arr = np.array(arr)
        mul = np.array(mul)
        for i in range(len(nums)):
            val = arr[i]
            temp = mul[i]
            mul = val * mul
            mul[i] = temp
            print(temp, mul)
        return mul
