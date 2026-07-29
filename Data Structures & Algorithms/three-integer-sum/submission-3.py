class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        threesum = []
        num_sort = sorted(nums)
        left = 0
        right = len(num_sort) - 1
        for i in range(len(num_sort)):
            left = i + 1
            right = len(num_sort) - 1
            while left < right:
                if num_sort[left] + num_sort[right] + num_sort[i] == 0:
                    if [num_sort[left],num_sort[right],num_sort[i]] not in threesum:
                        threesum.append([num_sort[left],num_sort[right],num_sort[i]])
                    left += 1
                    right = len(num_sort) - 1
                elif num_sort[left] + num_sort[right] + num_sort[i] < 0:
                    left += 1
                else:
                    right -= 1
            
        return threesum