class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        '''prefix = [0] *(len(nums))
        for i in range(len(nums)):
            prefix[i] = prefix[i-1] +nums[i]
        return prefix  '''
        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums    