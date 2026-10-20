class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        max_b = 0
        count = 0
        l = 0
        for r in range(n):
    
            if blocks[r] == 'B':
                count += 1
        
    
            if r >= k:
                if blocks[l] == 'B':  
                    count -= 1
                l += 1                
        
   
            if r >= k - 1:
                max_b = max(max_b, count)
        return k - max_b