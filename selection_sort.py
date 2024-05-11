def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        small = nums[i]
        index = i
        for j in range(i + 1, n):
            if small > nums[j]:
                small = nums[j]
                index = j
        if index != i:
            nums.insert(i, nums.pop(index))
    return nums


if __name__ == "__main__":
    print(selection_sort([-1, 3, 5, 1, 4, 8, 3, -10]))
