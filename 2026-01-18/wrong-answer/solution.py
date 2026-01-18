class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        sumList = []

        
        for num in nums:
            goal = target - num
            if goal in prevMap:
                sumList.append(goal,num)
                print(sumList)
                return sumList
                