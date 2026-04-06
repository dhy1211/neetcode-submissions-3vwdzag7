class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s)) # dấu ''.join để ghép lại với nhau vd : sorted biến nó thành ("a","e","t"), ''.join sẽ biến nó thành "aet"

            res[sorteds].append(s)
        return list(res.values())

        
        