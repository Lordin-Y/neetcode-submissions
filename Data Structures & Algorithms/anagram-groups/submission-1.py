class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we can create a hashmap 
        #if char's are different  we add a new list
        #fingerprint = "".join(sorted(word))
        #if char are the same, add it to the list that has the same char's
        #fingerprint = "".join(i)
        hash_map = {}
        if not strs:
            return []
        for word in strs:
            fingerprint = "".join(sorted(word))
            if fingerprint not in hash_map:
                hash_map[fingerprint] = [word]
            else:
                hash_map[fingerprint].append(word)
        return list(hash_map.values())
            
                
        
                    