"""Min and Max in Array"""

class Solution:
    def getMinMax(self, arr):
        arr.sort()
        k = []
        k.append(arr[0])
        k.append(arr[-1])
        return k