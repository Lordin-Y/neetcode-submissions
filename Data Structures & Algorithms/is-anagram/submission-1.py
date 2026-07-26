class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnts = Counter()
        cntt = Counter()
        
        if len(s) != len(t):
            print("False")
        for letters in s:
            cnts[letters] += 1
        for lettert in t:
            cntt[lettert] += 1
        if cntt == cnts:
            return True
        else:
            return False
            