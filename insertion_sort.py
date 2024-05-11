def insertion_sort(nums: list) -> list:
    n = len(nums)
    for i in range(n):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

    return nums

if __name__ == '__main__':
    print(insertion_sort([-1, 3, 5, 1, 4, 8,3,-10,0]))
