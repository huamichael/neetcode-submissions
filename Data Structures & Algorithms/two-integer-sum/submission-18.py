class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            try: 
                numDict[nums[i]].append(i)
            except:
                numDict[nums[i]] = [i]

        for i in range(min(nums),(target+abs(min(nums)))//2+1):
            try:
                ans = [min(numDict[i]), max(numDict[target-i])]
                return [min(ans),max(ans)]
            except:
                continue