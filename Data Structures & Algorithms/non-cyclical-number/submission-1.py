class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.sumall(n)
            
            if n == 1:
                return True
        return False

    def sumall(self, n: int) -> int:
        s = 0
        for digit in str(n):
            s += int(digit) ** 2
        return s