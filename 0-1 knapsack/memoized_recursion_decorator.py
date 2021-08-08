def memoize(func):
    memo = {}
    def helper(n, t):
        if (n,t) not in memo:
            memo[(n,t)] = func(n, t)
        return memo[(n,t)]
    return helper

@memoize
def knapsack(n, target):
    if not target:
        return True
    if n == 0 and target:
        return False
    if nums[n] <= target:                
        return knapsack(n-1, target - nums[n]) or knapsack(n-1, target)
    else:
        return knapsack(n-1, target)
