class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #for letter in string
        #r pointer goes through letter, storing info
        #once duplicate substring hit,
        #move l until no duplicates
        #record length of substring
        #return longest length
        l = 0
        max_length = 0
        substrings = set()
        for r in range(len(s)):
            while s[r] in substrings:
                substrings.remove(s[l])
                l += 1
            substrings.add(s[r])
            if max_length < r - l + 1:
                max_length = r - l + 1
        return max_length
        
