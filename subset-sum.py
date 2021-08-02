  def dynIsSubset(nums, sum):
  	dp = np.zeros(len(set)+1, sum+1)
  	
    for s in range(1, sum+1):
        for n in range(1,len(nums)+1):
      	if s == 0:
        	dp[s][n] = True
      	elif s !=0 and n==0:
        	dp[s]][n] == False
        else:
      	    if set[s][n] <= s:
        	    dp[s][n] = dp[s][n-1] or dp[s-nums[n]][n-1]
            else:
        	    dp[s][n] = dp[s][n]
    return dp[sum][len(nums)]
