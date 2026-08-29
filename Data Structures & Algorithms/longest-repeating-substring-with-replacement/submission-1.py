class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_substring = 0
        chr_set = set(s)
        for c in chr_set:
            l = 0
            count = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                while (r-l+1)-count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                    
                max_substring = max(max_substring, r-l+1)
        return max_substring


        #for each chr in chr set
        # if chr in the string is the character
        #problem
        # k = 2, XXXYYYYYYYYY
        # replacing first will give
        # XXXXXYYYY or smth
        #solution: decrease window when 
        #num of non chr exceeds k
