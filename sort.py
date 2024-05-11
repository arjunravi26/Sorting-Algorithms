from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
import sys

class Sort:
    def __init__(self, arr) -> None:
        self.arr = arr

    def bubble_sort(self) -> list:
        return bubble_sort(self.arr.copy())

    def selection_sort(self) -> list:
        return selection_sort(self.arr.copy())

    def insertion_sort(self) -> list:
        return insertion_sort(self.arr.copy())


if __name__ == "__main__":
    nums = [-1, 3, -2, 4, 2, 8, 7]

    numbers = input(
        f"Enter numbers seperated by spaces to sort:   (if nothing entered the default values will be {nums})\n"
    )
    sort_type = int(
        input(
            "Enter the type of sorting algorithm you want \n1 for bubble sort\n2 for selection sort\n3 for insertion sort\n"
        )
    )
    if sort_type not in range(1, 4):
        print("Invalid Option")
        sys.exit()
        
    try:
        numbers = [int(num) for num in numbers.split()]
        if not numbers:
            numbers = nums
        obj = Sort(numbers)
        if sort_type == 1:
            sorted_array = obj.bubble_sort()
        elif sort_type == 2:
            sorted_array = obj.selection_sort()
        elif sort_type == 3:
            sorted_array = obj.insertion_sort()
        print(sorted_array)

    except ValueError as e:
        print(f"Invalid input! Enter number only \n {e}")
        sys.exit()
