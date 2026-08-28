class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #instead of hash tables,
        # have letters correspond to frequency arr.
        # each array stores count of letter
        #iterate through both strings, +=1 for s,
        # -=1 for t
        freq = [0] * 26
        for i in range(len(s)): #for accessing t
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        for i in freq:
            if i != 0:
                return False
        return True