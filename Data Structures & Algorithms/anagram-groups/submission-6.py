class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs :
            newstrs = ''.join(sorted(i))
            res[newstrs].append(i)
        return list(res.values())



        
        