class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # ------- O(N) -------------
        # a = 0
        # while a < len(nums):
        #     if nums[a] == target:
        #         return a
        #     elif nums[a] > target:
        #         nums.insert(a, target)
        #         return a
        #     else:
        #         a += 1
        # nums.append(target)
        # return(len(nums)-1)

        # -------- O(logN) -----------
        left, right = 0 , len(nums)-1
        while left <= right:
            mid =  (left+right) // 2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return left
