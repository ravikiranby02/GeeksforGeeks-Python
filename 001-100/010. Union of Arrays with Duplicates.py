class Solution:    
    def findUnion(self, a, b):
        r = set(a)
        k = set(b)
        return r | k
