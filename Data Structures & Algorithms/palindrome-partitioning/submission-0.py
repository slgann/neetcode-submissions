class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def find(start, path):
            if start == len(s):
                res.append(path.copy())
                return
            
            for end in range(start, len(s)):
                sub = s[start:end+1]
                if sub == sub[::-1]:
                    path.append(sub)
                    find(end+1, path)
                    path.pop()
        find(0, [])
        return res