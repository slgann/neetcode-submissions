class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for c in strs:
            count = [0] * 26
            for charr in c:
                count[ord(charr) - ord('a')] += 1
            dic[tuple(count)].append(c)
        return list(dic.values())