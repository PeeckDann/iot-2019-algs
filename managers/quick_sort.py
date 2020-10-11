from managers.swap import swap

class QuickSort:

    def __init__(self):
        self.number_of_comparisons = 0
        self.number_of_swaps = 0

    def sort_counter(self, puzzle_list, key=lambda obj: obj):
        self.number_of_comparisons = 0
        self.number_of_swaps = 0

        length = len(puzzle_list)

        self.sort(puzzle_list, 0, length - 1,  key)

        print("\n----------Quick Sort----------\nComparisons: {};\nSwaps: {}.\n"
              .format(self.number_of_comparisons, self.number_of_swaps))

    def sort(self, puzzle_list, start, end, key):
        if start < end:
            pivot = self.partition(puzzle_list, start, end, key)
            self.sort(puzzle_list, start, pivot - 1, key)
            self.sort(puzzle_list, pivot + 1, end, key)

    def partition(self, puzzle_list, start, end, key):
        pivot = puzzle_list[end]

        i = (start - 1)

        for j in range(start, end):
            self.number_of_comparisons += 1
            if key(puzzle_list[j]) < key(pivot):
                self.number_of_swaps += 1
                i += 1
                swap(puzzle_list, i, j)

        self.number_of_comparisons += 1
        swap(puzzle_list, i + 1, end)

        return i + 1
