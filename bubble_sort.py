def bubble_sort(arr: list) -> list:
    n = len(arr) - 1
    for i in range(n):
        for j in range(0, n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    print(bubble_sort([-1, 3, 5, 1, 4, 8,3,-10,0]))