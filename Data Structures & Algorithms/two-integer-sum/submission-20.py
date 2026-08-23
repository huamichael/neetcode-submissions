class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, n in enumerate(nums):
            hash_map[n] = i #hashmap keys are the values in nums
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash_map and hash_map[diff] != i:
                return [i, hash_map[diff]]


