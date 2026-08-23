class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create hash table
        # for i in nums
        # increment key's value by 1 corresponding
        # sort the hash table
        # return the k highest values
        hash_table = {}
        for i in nums:
            hash_table[i] = hash_table.get(i,0)+1
        array = []
        for num, count in hash_table.items():
            array.append([count, num])
        array.sort()
        
        highest_values = []
        while len(highest_values) < k:
            highest_values.append(array.pop()[1]) #pop returns list and last element in array
        return highest_values
