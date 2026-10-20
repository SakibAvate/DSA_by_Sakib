class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        win = sum(nums[:k])
        max_sum = win

        for i in range(k,len(nums)):
            win += nums[i] - nums[i-k]
            max_sum = max(max_sum,win)
        return max_sum/k  
        