class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = 0
        while num != 0:
            n = n + 1
            if num == 0:
                break
            elif num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
        return n
