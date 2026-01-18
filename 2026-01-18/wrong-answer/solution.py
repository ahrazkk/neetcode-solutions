class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        sumList = []

        
        for num in nums:
            goal = target - num
            if goal not in prevMap:
                prevMap[num] = goal
                print(prevMap)
            elif goal in prevMap:
                print(meow)
                
                