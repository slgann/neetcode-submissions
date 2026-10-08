class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new = self.toint(digits) + 1
        return list(str(new))
    

    def toint(self, digits: List[int]) -> List[int]:
        s = 0
        n = len(digits)
        for i in range(n):
            s += digits[i] * (10 ** (n-1-i))
        return s
    
        