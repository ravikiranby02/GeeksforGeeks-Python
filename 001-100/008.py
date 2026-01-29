"""Row Sum in a Matrix"""

class Solution:
    def rowSum(self, mat):
        r = []
        for row in mat:
            r.append(sum(row))
        return r
        