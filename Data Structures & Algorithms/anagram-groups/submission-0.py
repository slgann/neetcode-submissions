from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        
        for c in strs:
            # 修正 1 & 2：將 sorted 後的列表轉回字串，並轉為 tuple 作為 Key
            key = tuple(sorted(c))
            mapping[key].append(c)
            
        # 修正 3：使用 .values() 並轉換成 list 回傳
        return list(mapping.values())
