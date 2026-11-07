class Solution:
    def countDigits(self, num: int) -> int:
        count, dig = 0,0
        x = num
        while x>0:
            dig = x%10
            if num %dig == 0:
                count+=1
            x= x//10    
        return count    
        