class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num  
        return result
nums = [4, 1, 2, 1, 2]
solution = Solution()
print(solution.singleNumber(nums))
