#all subsets of a set (eg. [1,2,3])
def subsets(array):
    result = []
    
    def helper(index, path):
        result.append(list(path))
        
        for i in range(index, len(array)):
            path.append(array[index])
            helper(index+1, path)
            path.pop()
    
    helper(0,[])
    return result 

print(subsets([1,2,3]))
