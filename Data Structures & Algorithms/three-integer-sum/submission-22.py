class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if nums[i] == nums[i-1] and i > 0:
                continue
            while left < right:

                if nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                else:
                    output.append([nums[left],nums[right],nums[i]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return output
