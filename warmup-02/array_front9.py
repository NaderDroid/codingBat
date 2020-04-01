def array_front9(nums):
    val = 0
    while val < len(nums):
        if nums[val] == 9 and val < 4:
            return True
        elif val > 3:
            return False
        val += 1
        # else:
        #     print(n)
        #     return False


print(array_front9([1, 2, 3, 4, 9]), "check this one here too")
print(array_front9([1, 9, 9]), "check this one")
print(array_front9([1, 2, 9, 3, 4]))
print(array_front9([1, 2, 3, 4, 9]))
print(array_front9([1, 2, 3, 4, 5]))
print(array_front9([1, 9, 2, 3, 4, 5, 9, 6]))
