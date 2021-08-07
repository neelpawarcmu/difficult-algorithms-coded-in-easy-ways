class Solution:
    def isSubseq(self, sstr,lstr):
        smallerLength = min(len(sstr),len(lstr))
        dp = [[0 for col in range(len(lstr)+1)] for row in range(len(sstr)+1)]
        #dp rows,0 and 0,cols = 0
        for row in range(1, len(sstr)+1):
            for col in range(1, len(lstr)+1):
                if sstr[row-1] == lstr[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
        return dp[len(sstr)][len(lstr)] == smallerLength
        
        
#sol = Solution()
#a = "hello"
#b = "helli"
#print(sol.isSubseq(a,b))
