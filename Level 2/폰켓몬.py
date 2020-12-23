import collections

def solution(nums):
    count = len(nums)//2
    nums = dict(collections.Counter(nums))
    if count <= len(nums.keys()):
        return count
    else:
        return len(nums.keys())