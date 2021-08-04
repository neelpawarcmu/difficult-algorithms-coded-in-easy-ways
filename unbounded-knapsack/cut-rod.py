class Solution:
    def memoize(self, r, l, p):
        memo = {}
        def helper(r, l, p):
            if (r,l,p) not in memo:
                memo[(r,l,p)] = self.cutRodRec(r, l, p)
            return helper
    
    def cutRodRec(self, rod, lengths, prices):
        if not rod or not lengths:
            return 0
        n = len(lengths) - 1
        maxPrice = -1
        if lengths[n] <= rod:
            return max(self.cutRod(rod-lengths[n], lengths, prices), self.cutRod(rod, lengths[:n], prices[:n]))
        else:
            return self.cutRod(rod,lengths[:n], prices[:n])
            
         
    def cutRod(self, rod, lengths, prices):
        n = len(lengths)
        dp = [[0 for col in range(rod+1)] for row in range(n+1)]
        
        for l in range(1, n+1):
            for r in range(1, rod+1):
                if lengths[l-1] <= r:
                    dp[l][r] = max(prices[l-1] + dp[l-1][r-lengths[l-1]], dp[l-1][r])
                else:
                    dp[l][r] = dp[l-1][r]
        return dp[n][rod]
