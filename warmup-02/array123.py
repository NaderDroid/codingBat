def array123(nums):
    for n in range(len(nums)):
        if nums[n] == 1 and (n+2) < len(nums):
            if nums[n+1] == 2 and nums[n+2] == 3:
                return True
    else:
        return False


print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))
print(array123([1, 2, 3, 4, 5, 6]))
