class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {']' : '[', '}' : '{', ')' : '('}
        stack = []
        for char in s:
            if char in hash_map:
                # this is a CLOSING bracket — do your 3-step check here
                if stack and stack[-1] == hash_map[char]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                # this is an OPENING bracket — what do you do?
                
                    stack.append(char)
        return not stack