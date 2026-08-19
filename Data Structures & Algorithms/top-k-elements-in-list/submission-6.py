class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we count each value using a hashmap. This gives O(n) time and space. 
        #key = value at index, value = the count found for that value
        #now create an empty array with size + 1 that contains lists
        #we need a + 1 just in case there's an ex like #2, we need the extra list to store the counts of 7
        #Now we increment backwards from out 
        #use buckets so we don't have to go through sorting
        #.items() goes through key value pairs in a hashmap
        #index in buckets is how many times element appears. Value
        #element in buckets is the key. What number is being counted
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                hash_map[nums[i]] += 1 #{1 appears 1. Key:Value}
        #create buckets, this beats sorting O(nlgn)
        buckets = []
        for _ in range(len(nums)+ 1): #+1 to account for the counts appearing 6 times
            buckets.append([])#creates empty buckets
        for key,value in hash_map.items():
            buckets[value].append(key)
        result = []
        for i in range(len(buckets)-1, -1, -1):
            #need to go through the list at buckets[i]
            for num in buckets[i]:
                #append the element at position i in bucket
                #append the first k elements
                result.append(num)
                if len(result) == k:
                    return result