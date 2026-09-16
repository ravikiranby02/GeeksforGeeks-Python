class Solution:
    def prefSum(self, arr):
        total_sum = []
        count = 0
        for i in arr:
            count += i
            total_sum.append(count)
        return total_sum
