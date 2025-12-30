class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        print(nums)
        res = []

        for index,items in enumerate(nums):
            itemsBefore = nums[:index]
            itemsAfter = nums[index+1:]

            items = itemsBefore + itemsAfter

            print(items)
            value = math.prod(items)
            print(value)
            res.append(value)
            print(res) 

        return res