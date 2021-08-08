import math
class Solution:
    def __init__(self):
            self.memo = {}
            
    def isScrambled(self, str1, str2):
        #i, j = 0, len(str)-1
        #BCs: lengths are unequal
        #   : both are empty
        #   : both are exact same 
        #   : both are not anagrams (can do without, just optimization?)
        #   : both have 1 length and are unequal (equal is checked earlier so just check if length is 1 and return False)
            
        def matchStrings(str1, str2):
            if len(str1) != len(str2):
                return False
            if not str1:
                return True
            if str1 == str2:
                return True
            if len(str1) == 1:
                return False
            flag_scrambled = False
            
            i, j = 0, len(str1)-1
            if (str1,str2) in self.memo:
                return self.memo[(str1,str2)]
            
            for k in range(i,j):
                #condn1 parts
                if (str1[i:k], str2[i:k]) in self.memo:               
                    left1 = self.memo[(str1[i:k], str2[i:k])]
                else:
                    left1 = matchStrings(str1[i:k], str2[i:k])
                    self.memo[(str1[i:k], str2[i:k])] = left1
                
                if str1[k+1:j], str2[k+1:j] in self.memo:               
                    right1 = self.memo[(str1[k+1:j], str2[k+1:j])]
                else:
                    right1 = matchStrings(str1[k+1:j], str2[k+1:j)
                    self.memo[(str1[k+1:j], str2[k+1:j])] = right1
                
                #condn2 parts
                if (str1[k+1:j], str2[i:k]) in self.memo:               
                    left2 = self.memo[(str1[k+1:j], str2[i:k])]
                else:
                    left2 = matchStrings(str1[k+1:j], str2[i:k])
                    self.memo[(str1[k+1:j], str2[i:k])] = left2
                
                if (str1[i:k], str2[k+1:j]) in self.memo:               
                    right2 = self.memo[(str1[i:k], str2[k+1:j])]
                else:
                    right2 = matchStrings(str1[k+1:j], str2[k+1:j)
                    self.memo[(str1[k+1:j], str2[i:k])] = right2
                
                #assemble conditions
                condition1 = left1 and right1
                condition2 = left2 and right2
                
                if condition1 or condition2:
                     flag_scrambled = True
                     break
            return flag_scrambled
         
        return matchStrings(str1, str2)
#gr eat -> ate gr

sol = Solution()
string1 = "coder" 
string2 = "ocrde"
print(sol.isScrambled(string1, string2))
