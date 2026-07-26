class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = []

        for i in range(len(nums)):
            if nums[i] in new_list:
                return True
            new_list.append(nums[i])
        return False
        