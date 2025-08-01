def frequent(nums):
    hash = {}
    for i in range(0,len(nums)):
        if nums[i] not in hash.keys():
            hash[nums[i]] = 1
        else:
            hash[nums[i]] += 1
    maxCountNumber =0
    maxCount = 0
    for key , value in hash.items():
        if(maxCount < value):
            maxCount = value
            maxCountNumber = key
    return maxCountNumber

nums = list(map(int, input().split()))
print(frequent(nums)) 