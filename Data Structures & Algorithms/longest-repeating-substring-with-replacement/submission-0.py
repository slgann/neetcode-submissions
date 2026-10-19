class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}         # 你的記帳本：紀錄目前視窗內每個字元的出現次數
        max_freq = 0       # 紀錄目前視窗中，出現頻率最高的字元的次數
        left = 0           # 視窗的左邊界（尾巴）
        max_length = 0     # 紀錄一路上看過的最大合法長度
        
        for right in range(len(s)):
            
            count[s[right]] = count.get(s[right], 0) + 1
            
            
            max_freq = max(max_freq, count[s[right]])
            
            
            if (right - left + 1) - max_freq > k:
                
                count[s[left]] -= 1
                left += 1  
            
            
            max_length = max(max_length, right - left + 1)
            
        return max_length