
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

EXAMPLE:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

'''

def twoSum(nums, target):
    seen = []
    for place, val in enumerate(nums):
	req = target - val
        if req in seen:
            return [seen.index(req), place]
        else:
            seen.append(val)
    print('not found any')
