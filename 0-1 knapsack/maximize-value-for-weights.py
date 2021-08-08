class Solution:
    def takeWeights(self, capacity, weights, values):
        numOfWts = len(weights) - 1
        dp =[[0 for col in range(capacity+1)] for row in range(numOfWts+1)]
        
        for w in range(numOfWts+1):
            for c in range(capacity+1):
                #curr_weight = weights[w-1]
                if weights[w-1] <= c:
                    dp[w][c] = max((values[w-1] + dp[w-1][c-weights[w-1]]), dp[w-1][c])
                else:
                    dp[w][c] = dp[w-1][c]
        return dp[numOfWts][capacity]

#Uncomment to test
#val = [60, 100, 120]
#wt = [10, 20, 30]
#W = 50
#sol = Solution()
#print(sol.takeWeights(W, wt, val)) 
