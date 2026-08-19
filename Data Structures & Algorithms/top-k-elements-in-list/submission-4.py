class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                hash_map[nums[i]] += 1

        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])
        for key, value in hash_map.items():
            buckets[value].append(key)
        result = []
        for i in range(len(buckets)-1,-1,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result