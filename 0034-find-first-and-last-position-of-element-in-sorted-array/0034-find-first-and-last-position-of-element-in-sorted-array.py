class Solution:
    def first(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1
        lb = n                          # default n instead of -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb

    def last(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1
        ub = n                          # the fix
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        lb = self.first(nums, target)
        if lb == n or nums[lb] != target:
            return [-1, -1]
        ub = self.last(nums, target)
        return [lb, ub - 1]