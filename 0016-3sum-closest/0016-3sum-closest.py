class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n =len(nums)
        best =  nums[0]+nums[1]+nums[2]

        for i in range(0,n-2):
            l= i+1
            r = n-1
            while l < r:
                s= nums[i] + nums[l] +nums[r]

                if abs(s-target)< abs(best - target):
                    best = s

                if s == target :
                    return s
                elif s< target:
                    l+=1
                else:
                    r-=1

        return best                        
        