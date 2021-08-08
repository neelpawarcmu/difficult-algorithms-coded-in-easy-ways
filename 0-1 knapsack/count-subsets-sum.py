def countSubsetsSum(nums, target):
  numLen = len(nums)
  dp = [[0 for col in range(target+1)] for row in range(numLen+1)]
  
  #for target = 0, subset sum always exists for any length of subset of nums
  for row in range(numLen+1):
    dp[row][0] = 1
    
  #start from 1 since initialization is done for 0th row, column
  for n in range(1, numLen+1):
    for t in range(1, target+1):
      dp[n][t] = dp[n][t- nums[n-1]] + dp[n][t]
      
  return dp[numLen][target]
  
#Uncomment to test
#nums = [1,3,4,5,7,10]
#target = 10
#print(countSubsetsSum(nums, target))
