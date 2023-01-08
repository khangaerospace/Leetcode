class Solution(object):
    def maximumWeath(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        List = []
        for i in range(len(accounts)):
            List.append(self.add(accounts[i]))
        n = len(List)
        biggest = self.largest(List,n)
        return biggest
    def add(self, array):
        sum = 0
        for i in range(len(array)):
            sum = sum + array[i]
        return sum


    def largest(self, arr, n):

        # Initialize maximum element
        max = arr[0]

        # Traverse array elements from second
        # and compare every element with
        # current max
        for i in range(1, n):
            if arr[i] > max:
                max = arr[i]
        return max
