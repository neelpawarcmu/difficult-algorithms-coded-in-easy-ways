class Solution(object):
    def subsets(self, nums):
        dp = [[] for num in nums]
        dp[0].append([])
        dp[0].append([nums[0]])
        
        for idx,num in zip(range(1, len(nums)), nums[1:]):
            for subset in dp[idx-1]:
                dp[idx].append(subset)
                dp[idx].append(subset+[num])
                
        return dp[len(nums)-1]
    
            
        #initialize an empty set and a filled set, now for every combination in next step, use empty set and filled set, ffilling and not filling both to generate all combinations, and so on. 
