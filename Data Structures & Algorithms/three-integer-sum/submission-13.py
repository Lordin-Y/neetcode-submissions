class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #runtime = O(nlgn)
        #space = O(n)
        nums.sort()
        output = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1 
            while left < right:
                if nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                else:
                    triple = [nums[left], nums[right], nums[i]]
                    output.append(triple)
                    #found a match, now inc and dec left and right to keep discorvering
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return output

