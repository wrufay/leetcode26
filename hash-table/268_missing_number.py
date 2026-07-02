class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # use a hashmap
        # create the hash table and put everything in it
        # ok its a set
        my_set = set()

        for num in nums:
            my_set.add(num)
        
        # aight im struggling with indices per usual
        # gen needs to be drawn out for gen also like this is a recurring weakness
        for i in range(0, len(nums) + 1):
            if i not in my_set:
                return i
        
        # there is also a faster O(1) solution using math trick but ok
        