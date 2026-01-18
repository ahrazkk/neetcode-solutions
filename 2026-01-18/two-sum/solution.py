class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        PrevMap = {}
        # To sove this problem, we need a map of what exists in HashMap, a number that is target subtract c.num


        # Go through array with its indexes
        for i,n in enumerate(nums):
            snum = target - n #specify what second number get is needed

            if snum in PrevMap: # if second number existsm then return both
                return [PrevMap[snum],i]

            else: # otherwise map the values to prevMap
                PrevMap[n] = i