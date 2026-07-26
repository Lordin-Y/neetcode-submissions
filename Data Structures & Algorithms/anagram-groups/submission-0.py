class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we can create a hashmap 
        #if char's are different  we add a new list
        #if char are the same, add it to the list that has the same char's
        
        hash_map = {}
        for word in strs:
            fingerprint = "".join(sorted(word))
            if fingerprint in hash_map:
                hash_map[fingerprint].append(word)
            else:
                hash_map[fingerprint] = [word]
        return list(hash_map.values())
                    