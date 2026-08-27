class Solution:
    def isPalindrome(self, s: str) -> bool:
        #bf
        #strip all spaces, capitals, ignore numbers
        #for each letter, check if number at last is ==

        #optimal
        #make 2 pointers
        clean_s = []
        for i in s:
            if i.isalnum():
                clean_s.append(i)
        if clean_s == []:
            return True
        clean_s = ''.join(clean_s)
        clean_s = clean_s.lower()
        if len(clean_s) == 1:
            return True
        
        i = 0
        j = -1
        for letter in range(len(s)//2):
            if clean_s[i] == clean_s[j]:
                i += 1
                j -=1
            else:
                return False
        return True
