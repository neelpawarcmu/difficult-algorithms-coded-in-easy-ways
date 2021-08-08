import math
class Solution:
    def __init__(self):
        self.memo = {}
            
    def dropEggs(self, eggs, floors):
        #i, j = need to drop from 1st floor to number of floors thus, 1 to floors+1
        #BCs: just one floor: return 1
        #   : just one egg: return floors
        #   : no eggs or no floors: no trials 
        
        i, j = 1, floors+1
        
        if eggs == 1:
            return floors
        if eggs == 0 or floors == 0:
            return 0
        if floors == 1:
            return 1
        
        if (eggs,floors) in self.memo:
            return self.memo[(eggs,floors)]
        
        
        minCount = math.inf 
        #k range: full range of i to j
        for k in range(i, j):
            if (eggs, floors-k) not in self.memo:
                nobrkCount = self.dropEggs(eggs, floors-k)
                self.memo[(eggs, floors-k)] = nobrkCount
                
            if (eggs-1, k-1) not in self.memo:
                brkCount = self.dropEggs(eggs-1, k-1)
                self.memo[(eggs-1, k-1)] = brkCount
                
            tempcount = 1 + max(self.memo[(eggs, floors-k)], self.memo[(eggs-1, k-1)]) #+1 for current drop
            minCount = min(minCount, tempcount)
            self.memo[(eggs,floors)] = minCount
        return self.memo[(eggs,floors)]
                
                
sol = Solution()
eggs = 2
floors = 10
print(sol.dropEggs(eggs, floors))
