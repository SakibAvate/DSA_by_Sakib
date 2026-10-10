class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0
        j= 0
        for i in range(len(nums)):

            if nums[i] != val:
                nums[i] , nums[j] = nums[j] , nums[i]
                count +=1
                j+=1
        return count        