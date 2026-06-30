"""Minimum Sum of Absolute Differences of Pairs"""

class Solution:
    def findMinSum(self, A,B,N):
        total = 0
        R = sorted(A)
        K = sorted(B)
        for i in range(N):
            total += abs(R[i] - K[i])
        return total