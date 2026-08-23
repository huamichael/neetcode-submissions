class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert nums into hash map
        count = 0
        hash_nums = set(nums)
        # check for consecutive sequence
        # if the number before doesnt exist, it is the
        # start
        # otherwise, look at the next number
        for num in hash_nums:
            if (num - 1) not in hash_nums:
                length = 1
                while (num + length) in hash_nums:
                    length += 1
                count = max(length, count)
        return count

        