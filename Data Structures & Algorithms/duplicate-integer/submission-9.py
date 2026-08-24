class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = set(nums)
        if len(hash_table) < len(nums):
            return True
        return False