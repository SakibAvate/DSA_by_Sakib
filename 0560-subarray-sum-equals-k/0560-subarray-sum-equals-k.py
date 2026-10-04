class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0 : 1}
        count = 0
        curr = 0

        for num in nums:
            curr += num
            count += freq.get(curr - k,0)
            freq[curr] = freq.get(curr,0)+1
            
        return count