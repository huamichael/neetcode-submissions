class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #bf: sort both str, check if ==
        #sorted has O(nlogn)
        #O(slogs + tlogt)

        #anagrams have:
        #equal len
        #equal frequency of letters

        if len(s) != len(t):
            return False
        hash_s = {}
        hash_t = {}
        for i in range(len(s)):
            hash_s[s[i]] = hash_s.get(s[i], 0) + 1
            hash_t[t[i]] = hash_t.get(t[i], 0) +1
        if hash_s == hash_t:
            return True
        return False

        
        