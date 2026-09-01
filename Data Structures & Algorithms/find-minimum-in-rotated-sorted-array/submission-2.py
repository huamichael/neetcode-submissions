class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        # get out of the loop as soon as l == r because that is where the minimum will be at
        while l < r:
            m = (l + r) // 2

            # pivot/resets on the right so search right side
            if nums[m] > nums[r]:
                l = m + 1

            # pivot/resets on the left  so search left side but don't lose current minimum value
            elif nums[l] > nums[m]:
                r = m

            # otherwise, it is a traditional binary search which means L pointer will always be the minimum
            elif nums[l] <= nums[m] <= nums[r]:
                return nums[l]

        return nums[l]