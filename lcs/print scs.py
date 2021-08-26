class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[0 for col in range(len(str2)+1)] for row in range(len(str1)+1)]
        
        for row in range(1, len(str1)+1):
            dp[row][0] = 0 
        for col in range(len(str2)+1):
            dp[0][col] = 0 

        for row in range(1, len(str1)+1):
            for col in range(1, len(str2)+1):
                if str1[row-1] == str2[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
                    
        row, col = len(str1), len(str2)
        
        superSeq = ""
        while row and col:
            if str1[row-1] == str2[col-1]:
                superSeq = str1[row-1] + superSeq
                row-=1
                col-=1
            else:
                if dp[row-1][col] > dp[row][col-1]:
                    superSeq = str1[row-1] + superSeq
                    row-=1
                else:
                    superSeq = str2[col-1] + superSeq
                    col-=1
        while row:
            superSeq = str1[row-1] + superSeq
            row-=1
        while col:
            superSeq = str2[col-1] + superSeq
            col-=1
            
        return superSeq
