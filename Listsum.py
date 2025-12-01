class Solution(object):
    def twoSum(self, nums, target):
        s = {}
        for ind, value in enumerate(nums):
            if target - value in s:
                return [s[target - value], ind]
            s[value] = ind
        return []
