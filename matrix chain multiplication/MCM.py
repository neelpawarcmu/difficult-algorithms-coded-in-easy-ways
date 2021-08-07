class Solution:
    def MCM(self, array, strt, end):
        
        if strt>=end: #step2: BCs
            return 0
        
        minimum = math.inf
        
        for k in range(strt, end): #step 3: k loop: go till j-1 because at j, we have an empty array for k 
            temp = self.MCM(array, strt, k) + self.MCM(array, k+1, end) + (array[strt-1]*array[k]*array[end])
           
            minimum = min(minimum, temp)
        
        return minimum
        
#sol = Solution()
#matrixArray = [40, 20, 30, 10, 30]
#step1: fix i, j
#s = 1 #one step ahead to accomodate i-1
#e = len(matrixArray) - 1 #normal because j-1 is ok
#print(sol.MCM(matrixArray, s, e))
