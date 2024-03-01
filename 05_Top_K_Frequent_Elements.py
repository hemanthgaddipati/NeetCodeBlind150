'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

'''



import heapq

def topKFrequent(nums, k):

    counter = {}
    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    heap = [(freq, num) for (num, freq) in counter.items()]
    heapq.heapify(heap)
    while len(heap) > k:
        heapq.heappop(heap)
    return [num for (freq, num) in heap]

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))