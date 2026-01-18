class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        
        for num in nums:
            goal = target - num
            print(goal)
            if goal in nums:
                return dict(goal)