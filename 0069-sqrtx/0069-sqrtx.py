class Solution:
    def mySqrt(self, x: int) -> int:

        left, right = 0, x
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans        

        ''' i=1
        while i*i <= x:
            i += 1
        return (i-1)  ''' 

        