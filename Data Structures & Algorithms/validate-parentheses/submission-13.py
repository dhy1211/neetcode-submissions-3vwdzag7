class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in dict1:
                if stack and stack[-1] == dict1[char]:
                        stack.pop()
                else :
                    return False
            else :
                stack.append(char)
        return not stack 
                

        