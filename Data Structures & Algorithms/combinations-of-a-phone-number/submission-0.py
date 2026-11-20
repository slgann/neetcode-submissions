class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        hmap = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        res = []

        def dfs(i, cur_str):
            if len(cur_str) == len(digits):
                res.append(cur_str)
                return
            
            letter = hmap[digits[i]]
            for s in range(len(letter)):
                dfs(i+1, cur_str + letter[s])
        dfs(0, '')
        return res