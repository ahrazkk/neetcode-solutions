class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nextMap = defaultdict(int) 

        sortedNums = sorted(nums)
        # print(sortedNums)
        count = 0

        for key,value in enumerate(sortedNums):
            nextMap[value] = value +1
            print(nextMap)

            if (value +1) in nextMap:
                count += 1 
                print(count)


        