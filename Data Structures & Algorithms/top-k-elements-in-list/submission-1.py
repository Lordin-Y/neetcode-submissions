class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        bucket = []
        for i in range(len(nums)):
            fingerprint = nums[i]
            if fingerprint in hash_map:
                hash_map[fingerprint] += 1
            else:
                hash_map[fingerprint] = 1
        for i in range(len(nums) + 1):
            bucket.append([])
        for key, value in hash_map.items():
            bucket[value].append(key)

        count = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                count.append(num)
            if len(count) == k:
                return count
            



