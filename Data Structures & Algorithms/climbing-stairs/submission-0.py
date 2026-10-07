class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        s1 = 1
        s2 = 2
        for _ in range(3, n+1):
            curr = s1 + s2
            s1 = s2
            s2 = curr
        return s2