
def removeElement(nums, val):
        k = 0
        nums.sort(key=lambda num: num == val)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 0
            else:
                k+=1
        return k, nums
        

k, nums = removeElement([0,1,2,2,3,0,4,2], 2)
[0,1,2,2,3,0,4,2]
[3,2,2,3]
print(nums)
print(k)

