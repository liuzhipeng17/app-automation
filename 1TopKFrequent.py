# 前K个高频元素

给定一个非空的整数数组，返回其中出现频率前k高的元素

nums = [1, 1, 1, 2, 2, 3],  k=2

def topKFrequent(nums, k):
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    
    res = []
    for key,value in d.items():
        if value = k:
            res.append(key)
            
    return res