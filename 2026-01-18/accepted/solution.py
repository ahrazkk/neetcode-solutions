class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}


        for index,numbers in enumerate(nums):
            goal = target - numbers
            print(goal)

            if goal not in prevMap:
                prevMap[numbers] = index
                print(prevMap)
            elif goal in prevMap:
                return [prevMap[goal],index]
        

    


                    