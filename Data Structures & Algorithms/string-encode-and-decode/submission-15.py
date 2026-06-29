class Solution:

    def encode(self, strs: List[str]) -> str:
        ket_qua =  ""
        for i in strs:
            ket_qua += str(len(i)) + "#" + i
        return ket_qua
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j + 1
        
            res.append(s[i: i + length]) 
        
            i += length
        
        return res 
