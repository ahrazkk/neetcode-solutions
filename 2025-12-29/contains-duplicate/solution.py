class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       #1.  Another way to solve it is using pythons vocab

       # By using lens, we can have it so that we compare the length of the original array to 
       # the array inside a set function removing duplicates, this way if their is a dupe
       # it will have the comparsions be different, and using !=, if they are different, then we return true

       return len(nums) != len(set(nums))