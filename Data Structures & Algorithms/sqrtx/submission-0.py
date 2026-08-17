class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x

        while l <= r:
            mid = (l+r)//2
            res = mid * mid
            if res == x:
                return mid
            if res < x:
                l = mid + 1
            else:
                r = mid -1
        
        return r