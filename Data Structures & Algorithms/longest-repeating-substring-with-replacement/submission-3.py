class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        resultLen = 0
        hash_map = {}
        for right in range(len(s)):
            if s[right] not in hash_map:
                hash_map[s[right]] = 1
            else:
                hash_map[s[right]] += 1
            while (right - left + 1) - max(hash_map.values()) > k:
                hash_map[s[left]] -= 1
                left += 1
            resultLen = max(right - left + 1, resultLen)
        return resultLen


