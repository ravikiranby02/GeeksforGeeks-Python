class Solution:
    def printTillN(self, n, current=1):
        if current > n:
            return
        
        print(current, end=" ")
        
        self.printTillN(n, current + 1)
