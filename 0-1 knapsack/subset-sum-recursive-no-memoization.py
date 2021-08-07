def isSubset(n, sum):
	if sum == 0:
  	return True
  if n == 0 and sum != 0:
  	return False
    
  if set[n] <= sum:
  	return isSubset(n-1, sum-set[n]) or isSubset(n-1, sum)
	else:
  	return isSubset(n-1, sum)
