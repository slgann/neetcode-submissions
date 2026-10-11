class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for n in tokens:
            if n == '+':
                s.append(s.pop() + s.pop())
            elif n == '-':
                a = s.pop()
                b = s.pop()
                s.append(b - a)
            elif n == '*':
                s.append(s.pop() * s.pop())
            elif n == '/':
                a = s.pop()
                b = s.pop()
                s.append(int(float(b) / a))
            else:
                s.append(int(n))
        return int(s[-1])