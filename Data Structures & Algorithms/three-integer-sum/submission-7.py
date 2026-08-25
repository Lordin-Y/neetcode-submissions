class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #runtime = O(nlgn)
        #space = O(n)
        nums = sorted(nums)
        output = []
        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                else:
                    triple = [nums[left], nums[right], nums[i]]
                    if triple not in output:
                        output.append(triple)
                    #found a match, now inc and dec left and right to keep discorvering
                    left += 1
                    right -= 1
        return output

