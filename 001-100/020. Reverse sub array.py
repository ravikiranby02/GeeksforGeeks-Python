class Solution:
    def reverseSubArray(self, arr, l, r):
        l -= 1
        r -= 1

        def helper(arr, left, right):
            if left >= right:   
                return
            arr[left], arr[right] = arr[right], arr[left]  
            helper(arr, left + 1, right - 1)               

        helper(arr, l, r)
        return arr
