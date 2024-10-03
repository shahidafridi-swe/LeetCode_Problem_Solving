class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        b=1
        while b<len(nums):
            if nums[a]==nums[b]:
                nums.pop(b)
            else:
                a +=1
                b +=1
        return len(nums)