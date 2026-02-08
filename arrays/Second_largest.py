def second_largest(nums):
    num1=max(nums)
    result=[]
    for i in nums:
        if i!=num1:
            result.append(i)
    return max(result)
print(second_largest([10, 5, 20, 8, 20]))
