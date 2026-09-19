class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
        
        top_k_keys = heapq.nlargest(k, dic, dic.get)
        return top_k_keys 
