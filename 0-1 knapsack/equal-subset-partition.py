#Q: can a set be partitioned into 2 subsets of equal sums?
#A: Just divide the set's full sum by two (and it needs to be even, right?) and do a subset sum search

class Solution(object):
    def canPartition(self, nums):
        def subsetSum(numLen, target):
            memo = [[False for col in range(target+1)] for row in range(numLen+1)]
            for n in range(numLen): #target = 0
                memo[n][0] = True
            #second base case need not be taken as initialization is all False
            
            for n in range(1, numLen+1):
                for t in range(1, target+1):
                    if nums[n-1] <= t:
                        memo[n][t] = memo[n-1][t - nums[n-1]] or memo[n-1][t]
                    else:
                        memo[n][t] = memo[n-1][t]
            return memo[numLen][target]
        
        totalSum = sum(nums) #O(n) time
        n = len(nums)
        
        
        if totalSum %2 == 1:
            return False
        else:
            return subsetSum(n, totalSum//2)
