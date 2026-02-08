def first_duplicate(nums):
    seen=set()
    for i in nums:
        if i in seen:
            return i
        seen.add(i)
print(first_duplicate([10, 5, 20, 8, 20]))
