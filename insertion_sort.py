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

"""
Insertion Sort

Swap if the left number is greather than right number. swap until its left side become less than it.
Time complexity:
Worst Case:O(N^2)
Average Case: O(N^2)
Best Case: O(N)
Space Complexity: O(1)

"""