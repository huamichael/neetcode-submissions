class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hash_table = {}
        t_hash_table = {}
        for i in range(len(s)):
            s_hash_table[s[i]] = s_hash_table.get(s[i], 0) + 1
            t_hash_table[t[i]] = t_hash_table.get(t[i], 0) + 1
        return s_hash_table == t_hash_table
        