def twoSum(nums, target):
    seen = []
    for place, val in enumerate(nums):
	req = target - val
        if req in seen:
            return [seen.index(req), place]
        else:
            seen.append(val)
    print('not found any')