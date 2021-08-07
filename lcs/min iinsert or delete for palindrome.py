class Solution:
    def minPalDeleteORInsert(self, string):
        rev = string[::-1]
        dp = [[0 for col in range(len(rev)+1)] for row in range(len(string)+1)]
        for row in range(1, len(string)+1):
            for col in range(1, len(rev)+1):
                if string[row-1] == rev[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
        
        lcsLength = dp[len(string)][len(rev)]
        return len(string) - lcsLength
        
#sol = Solution()
#a = "hello"
#print(sol.minPalDeleteORInsert(a))
