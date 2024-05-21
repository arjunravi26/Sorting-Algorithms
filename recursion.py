def nums(n):
    if n < 1:
        return n
    else:
        return nums(n - 1) + nums(n - 2)


print(nums(5))
