class Solution:
    def reverseArray(self, arr):
        
        left = 0
        right = len(arr) -1
        
        for i in range(len(arr) // 2):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr