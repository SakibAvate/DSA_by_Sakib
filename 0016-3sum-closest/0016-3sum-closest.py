class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if abs(s - target) < abs(best - target):
                    best = s

                if s == target:
                    return s
                elif s < target:
                    left += 1
                else:
                    right -= 1

        return best