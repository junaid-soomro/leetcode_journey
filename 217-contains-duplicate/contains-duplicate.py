class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct_val = {}
        for value in nums:
            if(value in distinct_val):
                return True
            distinct_val[value] = True

        return False 
