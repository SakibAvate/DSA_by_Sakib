class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        n =len(nums)
        myset =set(nums)
        longest = 0
        for s in myset:
            if s-1 not in myset:
                x = s
                count = 1
                while x+1 in myset:
                    count +=1
                    x +=1
                longest = max(longest , count )

        return longest