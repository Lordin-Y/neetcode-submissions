class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        #[2,3,4,5,10,20]
        length = 0
        longest = 0
        for i in num_set:
            if (i-1) not in num_set:
                length = 1
                while (i+1) in num_set:
                    length += 1
                    i += 1
                longest = max(longest, length)
        return longest
                

            