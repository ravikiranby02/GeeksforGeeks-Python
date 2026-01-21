"""Array Search"""

class Solution:
    def search(self, arr, x):
        
        for index in range(len(arr)):
            if arr[index] == x:
                return index
        return -1