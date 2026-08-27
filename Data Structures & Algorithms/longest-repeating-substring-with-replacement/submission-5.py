class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_table = {}
        left = 0
        count = 0
        for right in range(len(s)):
            if s[right] not in hash_table:
                hash_table[s[right]] = 1
            else:
                hash_table[s[right]] += 1
            if (right - left+1) - max(hash_table.values()) <= k:
                count = max(count, right - left + 1)
            else:
                hash_table[s[left]] -= 1
                left += 1
        return count