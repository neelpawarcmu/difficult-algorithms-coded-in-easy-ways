class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        dp = [['' for col in range(len(text2)+1)] for row  in range(len(text1)+1)]
        for row in range(1, len(text1)+1):
            for col in range(1, len(text2)+1):
                if text1[row-1] == text2[col-1]:
                    dp[row][col] = dp[row-1][col-1] + text1[row-1]
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])    
        return dp[len(text1)][len(text2)]
        
    #optimizing for space:
    def longestCommonSubsequenceOptimized(self, text1, text2):
        dp = [[0 for col in range(len(text2)+1)] for row  in range(len(text1)+1)]
        for row in range(1, len(text1)+1):
            for col in range(1, len(text2)+1):
                if text1[row-1] == text2[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])    
        
        lcs = ''
        t1, t2 = len(text1), len(text2)
        while t1 and t2:
            if text1[t1-1] == text2[t2-1]:
                lcs += text1[t1]
                t1 -= 1
                t2 -= 1
            else:
                if dp[t1][t2-1] > dp[t1-1][t2]:
                    t2 -= 1
                else:
                    t1 -= 1
        return lcs[::-1]
                
        
#Uncomment to test
#sol = Solution()
#text1 = 'abcde'
#text2 = 'zabcef'
#print(sol.longestCommonSubsequenceOptimized(text1,text2))
