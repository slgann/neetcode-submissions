class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heapq = []
        res = []
        if not points:
            return []
        
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dis = (x ** 2 + y ** 2) * (-1)
            heapq.heappush(max_heapq, (dis, points[i]))

            if len(max_heapq) > k:
                heapq.heappop(max_heapq)
        
        for p in max_heapq:
            res.append(p[1])
        return res
        