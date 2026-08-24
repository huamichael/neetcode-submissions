class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # all 3 #s in an arr where combined return 0
        #sort list
        # use 2 pointers start and end, and 1 pointer 
        # moving slowly
        # first pointer moves through nums
        # for each 1st pointer move, 
        # have 2 pointers move for all combos
        nums.sort()
        result = []
        for i, value in enumerate(nums):
            if value > 0:
                break # no negatives
            l = i+1
            r = len(nums) - 1
            #check to prevent duplicates
            if i > 0 and value == nums[i-1]:
                continue
            while l < r:
                #check for ans
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l +=1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return result