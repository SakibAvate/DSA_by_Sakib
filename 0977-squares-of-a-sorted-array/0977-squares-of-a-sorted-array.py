class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n =len(nums)
        res = [0] * n
        left = 0
        right = n-1
        i =n-1

        while left <= right:
            leftSq = nums[left]**2
            rightSq = nums[right]**2

            if leftSq > rightSq:
                res[i] = leftSq
                left +=1
            else:
                res[i] = rightSq
                right -= 1

            i -=1

        return res            

        