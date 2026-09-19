class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        
        for c in strs:
            # 修正 1 & 2：將 sorted 後的列表轉回字串，並轉為 tuple 作為 Key
            key = tuple(sorted(c))
            dic[key].append(c)
            
        # 修正 3：使用 .values() 並轉換成 list 回傳
        return list(dic.values())
