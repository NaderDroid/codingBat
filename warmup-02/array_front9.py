def array_front9(nums):
    print(len(nums))
    val = 0
    while val < len(nums):
        if nums[val] == 9 and val <= 3:
            return True
        elif val > 3 or val == (len(nums)-1):
            return False
        else:
            val += 1
    return False
    # else:
    #     print(n)
    #     return False


print(array_front9([]))
print(array_front9([1, 2, 3]))
print(array_front9([1, 2, 3, 4, 9]), "here too")
print(array_front9([1, 9, 9]), "check this one")
print(array_front9([1, 2, 9, 3, 4]))
print(array_front9([1, 2, 3, 4, 9]))
print(array_front9([1, 2, 3, 4, 5]))
print(array_front9([1, 9, 2, 3, 4, 5, 9, 6]))
