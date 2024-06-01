def bubble_sort(arr: list) -> list:
    n = len(arr) - 1
    for i in range(n):
        for j in range(0, n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    print(bubble_sort([-1, 3, 5, 1, 4, 8, 3, -10, 0]))

"""
Bubble Sort(Shrink Sort):

Here the first element get their correct possion is first iter,2nd element got in 2nd iter and so on.

Time Complexity:
Time complexity:
Worst Case:O(N^2)
Average Case: O(N^2)
Best Case: O(N)
Space Complexity: O(1)

"""
