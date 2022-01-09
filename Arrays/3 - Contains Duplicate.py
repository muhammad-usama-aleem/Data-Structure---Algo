'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true


Example 2:

Input: nums = [1,2,3,4]
Output: false
'''

def containsDuplicate(nums):
    # dup = []
    # for val in nums:
    #     if val in dup:
    #         return True
    #     if val not in dup:
    #         dup.append(val)
    # return False
    
    return (len(nums) != len(set(nums))) # simply check length of given array with its set
