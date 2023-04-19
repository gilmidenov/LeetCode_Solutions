class Solution:
    def isPalindrome(self, x: int) -> bool:
        d = x
        x2 = 0
        while d > 0:
            res = d % 10
            d = d// 10
            x2 = x2*10 + res
        if x == x2:
            return True
        else:
            return False