def missingNumber(nums) -> int:
    number = 0
    nums.sort()
    for i in range(len(nums)):
        print(i, nums[i])
        if i not in nums:
            number+=i  
    if len(nums) not in nums:
        number+=len(nums)
    return number
        
print(missingNumber([0,1]))