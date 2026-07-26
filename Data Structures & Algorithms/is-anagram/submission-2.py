class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = {}
        countt = {}

        for c in s:
            if c not in counts:
                counts[c] = 1
            else:
                counts[c] = counts[c] + 1
        
        for c in t:
            if c not in countt:
                countt[c] = 1
            else:
                countt[c] = countt[c] + 1
        
        if countt == counts:
            return True
        else:
            return False
            