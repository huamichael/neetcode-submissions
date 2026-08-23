class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       #sort each string, put first string in anagram array,
        #if second string matches first string put it in same array,
        #if not put it in separate array
        newdict = {}
        for i in strs:
            sortedi = ''.join(sorted(i))
            if sortedi not in newdict:
                newdict[sortedi] = [i]
            else:
                newdict[sortedi].append(i)
        return list(newdict.values())