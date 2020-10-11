import csv
import time

from models import puzzle
from managers import bubble_sort
from managers import quick_sort


if __name__ == '__main__':
    puzzle_list = []

    with open('puzzle_parameters.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            puzzle_list.append(puzzle.Puzzle(description=line[0], number_of_elements=line[1],
                                                    packaging_width=line[2], packaging_height=line[3]))

    bubble_sort = bubble_sort.BubbleSort()
    quick_sort = quick_sort.QuickSort()

    bubble_sort_start_time = time.time()
    bubble_sort.sort(puzzle_list, key=lambda puzzle_unit: puzzle_unit.number_of_elements)
    bubble_sort_end_time = time.time()
    print("List after Bubble Sorting:\n{}".format(puzzle_list))
    print("\nIt took {} seconds to Bubble Sort".format(bubble_sort_end_time - bubble_sort_start_time))

    quick_sort_start_time = time.time()
    quick_sort.sort_counter(puzzle_list, key=lambda puzzle_unit: puzzle_unit.packaging_height)
    quick_sort_end_time = time.time()
    print("List after Quick Sorting:\n{}".format(puzzle_list))
    print("\nIt took {} seconds to Quick Sort".format(quick_sort_end_time - quick_sort_start_time))
