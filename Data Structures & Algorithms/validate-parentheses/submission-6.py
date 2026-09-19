class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")" : "(" ,
            "]" :"[" ,
            "}" : "{"
        }
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if stack == []:
                    return False
                elif mapping.get(c) != stack[-1]:
                    return False
                stack.pop()
        return len(stack) == 0
         
        