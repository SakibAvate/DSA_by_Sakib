class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        score =0
        n = len(nums)
        for i in range(0, n+1):
            score += i
        return score - sum(nums)