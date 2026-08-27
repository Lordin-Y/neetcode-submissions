class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        hash_set = set()
        left = 0
        for right in range(len(s)):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
            hash_set.add(s[right])
            count = max(count, right - left + 1)
        return count
