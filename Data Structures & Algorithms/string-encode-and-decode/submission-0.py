class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes = []
        encoded_string = []
        for string in strs:
            sizes.append(len(string)) #sizes = [1,2,3,4]
        for size in sizes:
            encoded_string.append(str(size))
            encoded_string.append(',')
        encoded_string.append('#')
        encoded_string.extend(strs)
        return ''.join(encoded_string)
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i = 0
        sizes = []
        decoded_string = []
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(s[i:j])
            i = j + 1
        i += 1
        for size in sizes:
            decoded_string.append(s[i:(i+int(size))])
            i += int(size)
        return decoded_string
# ["a", "b, c", "d"]
# 1,12,13,14#asdfisdbfhud
# j = 0
# j = 1
# [4, 5, 3]

