'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

'''

def productExceptSelf(nums):
    prefix, postfix = 1, 1
    result = [1 for num in nums]
    for i in range(len(nums)):
        result[i] = prefix
        prefix = prefix * nums[i]
    for i in range(len(nums)-1, -1, -1):
        result[i] = result[i] * postfix
        postfix = postfix * nums[i]
    return result

print(productExceptSelf([1,2,3,4])) # result = [24,12,8,6]
print(productExceptSelf([-1,1,0,-3,3])) # result = [0,0,9,0,0]
