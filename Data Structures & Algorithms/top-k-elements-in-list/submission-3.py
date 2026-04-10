class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val = {}
        for i in nums:
            val[i] = 1 + val.get(i,0)
        arr = []
        for i, j in val.items():
            arr.append([j,i])
        arr.sort()            
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res 

    