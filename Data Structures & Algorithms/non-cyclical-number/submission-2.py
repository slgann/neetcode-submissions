class Solution:
    def isHappy(self, n: int) -> bool:
        def sumall(n:int) -> int:
            s = 0
            for d in str(n):
                s += int(d) ** 2
            return s
        
        slow = n
        fast = sumall(n)

        while fast != 1 and slow != fast:
            slow = sumall(slow)
            fast = sumall(sumall(fast))
        return fast == 1