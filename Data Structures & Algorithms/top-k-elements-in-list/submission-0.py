class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        ret = []
        for i in range(k):
            m = -1
            n = 0
            for key in d:
                if d[key] > m:
                    n = key
                    m = d[key]
            ret.append(n)
            d[n]=-1
        return ret