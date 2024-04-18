class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new_arr = []
        for index in range(len(nums)):
            new_arr.append(nums[nums[index]])


        return new_arr