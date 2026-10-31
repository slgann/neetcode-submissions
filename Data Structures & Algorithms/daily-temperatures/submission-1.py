class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n 
        stack = [] # 存索引值
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre_indx = stack.pop()
                res[pre_indx] = i - pre_indx
            
            stack.append(i)
        return res