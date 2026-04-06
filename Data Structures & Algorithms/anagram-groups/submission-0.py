class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s)) # dấu ''.join để sắp 
            res[sorteds].append(s)
        return list(res.values())

        
        