class Solution(object):
      def subsetSum(self, nums, target):
          numLen = len(nums)
          memo = [[False for col in range(target+1)] for row in range(numLen+1)]
          for n in range(numLen+1): #target = 0
              memo[n][0] = True
          #second base case need not be taken as initialization is all False

          for n in range(1, numLen+1):
              for t in range(1, target+1):
                  if nums[n-1] <= t:
                      memo[n][t] = memo[n-1][t - nums[n-1]] or memo[n-1][t]
                  else:
                      memo[n][t] = memo[n-1][t]
          return memo[numLen][target]

#Uncomment to test
#nums = [1,2,3,7]
#target = 11
#sol = Solution()
#print(sol.subsetSum(nums, target))
