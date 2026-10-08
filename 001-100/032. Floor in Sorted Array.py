class Solution:
    def findFloor(self, arr, k):
        n = len(arr)
        lb = -1               
        low, high = 0, n - 1  

        while low <= high:
            mid = (low + high) // 2        

            if arr[mid] <= k:
                lb = mid                   
                low = mid + 1              
                
            else:
                high = mid - 1             

        return lb                           