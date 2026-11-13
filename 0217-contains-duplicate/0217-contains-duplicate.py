class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set(nums)
        if len(nums) != len(seen):
            return True

        return False    

        