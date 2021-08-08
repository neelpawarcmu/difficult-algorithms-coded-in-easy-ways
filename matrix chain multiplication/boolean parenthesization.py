class Solution:
    def parenthesize(self, string):
        #steps
        #i, j = 0, len-1
        #extra isTrue variable (2T*4F = 8 example )
        #BCs
        #loop: k goes from -> i+1, step = 2, j-1
        l, r = 0, len(string)-1
        isTrue = True
        dp = {}
        
        
        def countWays(i, j, isTrue):
            #Base case
            if i > j:
                return 0
            if i == j:
                if isTrue:
                    return 1 if string[i] == "T" else 0
                else:
                    return 1 if string[i] == "F" else 0
            
            if (i,j,isTrue) in dp:
                return dp[(i,j,isTrue)]
            
            ans = 0 #temp answer
            for k in range(i+1, j, 2):
                LT = dp[(i,k,True)] if (i,k,True) in dp else countWays(i,k,True)
                
                LF = dp[(i,k,False)] if (i,k,False) in dp else countWays(i,k,False)
                
                RT = dp[(k+1,j,True)] if (k+1,j,True) in dp else countWays(k+1,j,True)
                
                RF = dp[(k+1,j,False)] if (k+1,j,False) in dp else countWays(k+1,j,False)


                if string[k] == "&":
                    if isTrue:
                        ans += LT*RT
                    else:
                        ans += LF*RT + LF*RF + LF*RF
                elif string[k] == "|":
                    if isTrue:
                        ans += LT*RT + LF*RT + LT*RF
                    else:
                        ans += LF*RF
                elif string[k] == "^":
                    if isTrue:
                        ans += LF*RT + LT*RF
                    else:
                        ans += LT*RT + LF*RF
                dp[(i,j,isTrue)] = ans
            return ans
            
        return countWays(l, r, isTrue)
        
string = "T|F&F"
sol = Solution()
print(sol.parenthesize(string))
