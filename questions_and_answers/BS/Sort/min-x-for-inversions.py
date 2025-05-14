


inf = float('inf')

###
### PROBLEM STATEMENT
###
"""
You are given an array of integers nums and an integer k.

An inversion pair with a threshold x is defined as a pair of indices (i, j) such that:

(1) i < j
(2) nums[i] > nums[j]
(3) The difference between the two numbers is at most x (i.e. nums[i] - nums[j] <= x).

Determine the minimum integer min_threshold such that there are at least k inversion pairs with threshold min_threshold.
If no such integer exists, return -1.
"""


###
### APPROACH
###
""" 
Standard binary search problem with an additional layer of complexity for counting inversions.

To start, given an array, you can naively count the number of inversions in O(N^2). 

for i in range(n):
  for j in range(i + 1, n):
    if nums[i] > nums[j]:
      invr += 1

One method of solving this would be the following:
Recall from algorithms, merge sort essentially recurses till a arrays of length 2 and then swaps the positions of the values if it is swapped.

This in itself is an inversion. What about when we are merging arrays of length 2? Say we have [3, 4] and [1, 2]. Since we already sorted them, 
if the 0th position of the 'left' array is less than the 0th position of the 'right' array, then we can add +2 inversions.

Notice that the count of inversions increase based off the size of the array.


This however, runs in O(NLog(N) * Log(N)) TC... could we do better?

Yes, with the usage of Segment Trees: https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/
"""


"""
Genearlized Merge Sort
"""
# def merge_sort(nums):
  # if len(nums) <= 1:
  #   return
  
  # split = n // 2
  
  # lS = merge_sort(nums[:split])
  # rS = merge_sort(nums[split:])

  # n = len(lS)
  # m = len(rS)

  # lp = rp = 0

  # while lp < n and rp < m:
  #   if lS[lp] <= rS[rp]:
      
  # return



def merge_sort(nums, threshold):
  """
  will be used to keep track of counts of inversions given threshold.
  """
  if len(nums) <= 1:
    return nums, 0
  n = len(nums)
  split = n // 2
  l, r = nums[:split], nums[split:]

  # Recurse
  lS, lC = merge_sort(l, threshold)
  rS, rC = merge_sort(r, threshold)

  merged = []
  invr = 0
  i = j = 0

  while i < len(lS) and j < len(rS):
    if lS[i] <= rS[j]: # no inversion
      merged.append(lS[i])
      i += 1
    else: # is inversion
      merged.append(rS[j])
      k = i
      while k < len(lS) and lS[k] > rS[j]:
        if lS[k] - rS[j] <= threshold:
          invr += 1
        k += 1
      j += 1
  
  merged.extend(lS[i:])
  merged.extend(rS[j:])
  invr = lC + rC + invr
  return merged, invr


def min_threshold(nums, k):
  lo, hi = 0, 10**9 + 100
  ret = inf
  while lo <= hi:
    mid = (lo + hi) // 2
    _, invr = merge_sort(nums, mid)
    if invr >= k:
      ret = min(ret, mid)
      hi = mid - 1
    else:
      lo = mid + 1
  return ret if ret != inf else -1

print(min_threshold([1,2,3,4,3,2,1], 7))