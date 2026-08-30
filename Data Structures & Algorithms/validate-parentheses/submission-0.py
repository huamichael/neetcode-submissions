class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chrs = {')':'(', '}': '{', ']': '['}
        for i in s:
            if i in chrs:
                if stack and stack[-1] == chrs[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack == []:
            return True
        return False