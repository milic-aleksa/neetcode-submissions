class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set(nums)
        if len(uniqueNums) == len(nums):
            return False
        else:
            return True