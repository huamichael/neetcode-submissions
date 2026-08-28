class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap2 = {}
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in hashmap:
                    hashmap[s[i]] += 1 
                else:
                    hashmap[s[i]] = 1
                if t[i] in hashmap2:
                    hashmap2[t[i]] += 1
                else:
                    hashmap2[t[i]] = 1
            if hashmap == hashmap2:
                return True
        return False