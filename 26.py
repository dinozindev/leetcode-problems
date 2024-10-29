def removeDuplicates(nums):
    k = 0
    unique_elements = []
    for i in range(len(nums)):
        if i+1 == len(nums) and nums[i] != nums[i-1]:
            k+=1
            unique_elements.append(nums[i])
            break
        elif i+1 == len(nums):
            k+=1
            break
        elif nums[i] == nums[i+1] or nums[i] not in unique_elements:
            k+=1
            unique_elements.append(nums[i])
    for value in unique_elements:
        for i in range(nums.count(value)-1):
            nums.remove(value)
    return nums, k, unique_elements

[1,1,2]
[0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates([1,2,3,4,5,6,7]))

class Solution:
    def removeDuplicates(self, nums) -> int:
        k = 0
        unique_elements = []
        for i in range(len(nums)):
            if i+1 == len(nums) and nums[i] != nums[i-1]:
                k+=1
                unique_elements.append(nums[i])
                break
            elif i+1 == len(nums):
                k+=1
                break
            elif nums[i] == nums[i+1] or nums[i] not in unique_elements:
                k+=1
                unique_elements.append(nums[i])
        for value in unique_elements:
            for i in range(nums.count(value)-1):
                nums.remove(value)
        
        return k 