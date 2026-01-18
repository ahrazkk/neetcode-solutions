class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        
        for num in nums:
            goal = target - num
            if goal in nums:
                return goal