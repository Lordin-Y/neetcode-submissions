class Solution:
    def findMin(self, nums: List[int]) -> int:
        lowest = float('inf')
        for i in range(len(nums)):
            lowest = min(lowest, nums[i])
        return lowest
        
