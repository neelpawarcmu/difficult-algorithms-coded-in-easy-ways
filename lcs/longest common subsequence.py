class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        dp = [[0 for col in range(len(text2)+1)] for row  in range(len(text1)+1)]
        for row in range(1, len(text1)+1):
            for col in range(1, len(text2)+1):
                if text1[row-1] == text2[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])    
        return dp[len(text1)][len(text2)]
      
#leetcode problem (1143)
