"""Second Largest"""

class Solution:
    def getSecondLargest(self, arr):
        filterd = list(set(arr))
        
        if len(filterd) < 2:
            return -1
        
        filterd.sort()
        return filterd[-2]