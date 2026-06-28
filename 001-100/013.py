"""1-D prefix sum"""

class Solution:
    def prefSum(self, arr):
        # code here
        total_sum = []
        count = 0
        for i in arr:
            count += i
            total_sum.append(count)
        return total_sum