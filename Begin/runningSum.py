class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        List = []
        for i in range(len(nums)):
            if i == 0:
                List.append(nums[0])
            else:
                add = nums[i] + List[i-1]
                List.append(add)
        return List


