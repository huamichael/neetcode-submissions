class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = 1
        suffix[n-1] = 1
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1] 
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(n):
            #must access the value to the left and right of i in prefix and suffix
            output.append(prefix[i] * suffix[i])
        return output
            
#account for negatives