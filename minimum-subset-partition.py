import math
class Solution(object):
    def minimumPartition(self, nums):
        def subsetSum(numLen, target):
          memo = [[False for col in range(target+1)] for row in range(numLen+1)]
          
          for n in range(numLen+1):
            memo[n][0] = True
          
          for n in range(1, numLen+1):
            for t in range(1, target+1):
              if nums[n-1] <= t:
                memo[n][t] = memo[n-1][t-nums[n-1]] or memo[n-1][t]
              else:
                memo[n][t] = memo[n-1][t]
          return memo[-1]
          
        def findMinDiff(allSumsPossible):
          minDiff = math.inf
          for summ in range(totalSum+1):
              if allSumsPossible[summ]:
                  diff = totalSum - 2*summ
                  minDiff = min(minDiff, diff) if diff>=0 else minDiff
          return minDiff
          
        length = len(nums)
        totalSum = sum(nums)
        allSumsPossible = subsetSum(length, totalSum)
        minDiff = findMinDiff(allSumsPossible)
        return minDiff
        

#main concept 1: treat totalSum of array as target
#main concept 2: minimize totalSum - 2*sum(subset1) -> this is equivalent to minimum of (sum(subset1) - sum(subset2))

#Uncomment to test
#sol = Solution()
#nums = [1,2,4,8]
#print(sol.minimumPartition(nums))
