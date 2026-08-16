class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sorts = {}
        sortt = {}
        for i in range(len(s)):
            if s[i] not in sorts:
                sorts[s[i]] = 1
            else:
                sorts[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in sortt:
                sortt[t[i]] = 1
            else:
                sortt[t[i]] += 1
        return sorts == sortt
       
        