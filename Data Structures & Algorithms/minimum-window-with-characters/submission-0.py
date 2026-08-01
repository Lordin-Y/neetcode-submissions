class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for i in range(len(t)):
            if t[i] not in need:
                need[t[i]] = 1
            else:
                need[t[i]] += 1

        window = {}
        have = 0
        needCount = len(need)
        result = ""
        resultLen = float("inf")
        left = 0
        for right in range(len(s)):
            c=s[right]
            if c not in window:
                window[c] = 1
            else:
                window[c] += 1
                
                
            if c in need and need[c] == window[c]:
                have += 1
            while have == needCount:
                if len(s[left:right + 1]) < resultLen:
                    result = s[left:right + 1]
                    resultLen = len(result)
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        return result