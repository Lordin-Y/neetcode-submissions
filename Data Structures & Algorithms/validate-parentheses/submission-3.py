class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {']' : '[', '}' : '{', ')' : '('}
        stack = []

        for c in s:
            if c in hash_map:
                #closing bracket
                if stack and stack[-1] == hash_map[c]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                #opening bracket
                stack.append(c)
        return not stack