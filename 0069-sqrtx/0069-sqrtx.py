class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2 :
            return x

        r = x     
        while r*r >x:
            r = (r + x //r)//2

        return r        

        ''' i=1
        while i*i <= x:
            i += 1
        return (i-1)  ''' 

        