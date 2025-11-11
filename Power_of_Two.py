class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0
sol = Solution()
print(sol.isPowerOfTwo(1))   
print(sol.isPowerOfTwo(16))  
