class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        hashTwo = {}

        if len(s) == len(t):
            for v in range(len(t)):

                if s[v] in hash:
                    hash[s[v]] += 1
                else:
                    hash[s[v]] = 1

                if t[v] in hashTwo:
                    hashTwo[t[v]] += 1
                else:
                    hashTwo[t[v]] = 1

            return hash == hashTwo
        return False