def countSubsetsSum(nums, target):
  numLen = len(nums)
  dp = [[0 for col in range(target+1)] for row in range(numLen+1)]
  
  #for target = 0, subset sum always exists for any length of subset of nums
  for row in range(numLen+1):
    dp[row][0] = 1
  #start from 1 since initialization is done for 0th row, column
  for n in range(1, numLen+1):
    for t in range(1, target+1):
      if nums[n-1] <= t:
        dp[n][t] = dp[n-1][t-nums[n-1]] + dp[n-1][t]
      else:
        dp[n][t] = dp[n-1][t]
  return dp[numLen][target]
  
  
def countSubsetsDiff(nums, diff):
  #diff = sum(subset1) - sum(subset2)
  #thus, diff = sum(subset1) - (totalSum - sum(subset1))
  #sum(subset1) = (totalSum + diff)/2
  totalSum = sum(nums)
  target = (totalSum + diff)//2
  return countSubsetsSum(nums, target)
  
  
#Uncomment to test
#nums = [0,1,3,5]
#diff = 2
#print(countSubsetsDiff(nums, diff))
