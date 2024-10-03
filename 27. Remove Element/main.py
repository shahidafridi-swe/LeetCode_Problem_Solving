class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        a = 0
        while a < len(nums):
            if nums[a] == val:
                nums.pop(a)
            else:
                a +=1
        return len(nums) 
        