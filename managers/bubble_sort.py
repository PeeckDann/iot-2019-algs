from managers.swap import swap


class BubbleSort:

    def __init__(self):
        self.number_of_comparisons = 0
        self.number_of_swaps = 0

    def sort(self, puzzle_list, key=lambda obj: obj):
        self.number_of_comparisons = 0
        self.number_of_swaps = 0

        length = len(puzzle_list)

        for i in range(length - 1):
            for j in range(0, length - i - 1):
                self.number_of_comparisons += 1
                if key(puzzle_list[j]) < key(puzzle_list[j+1]):
                    self.number_of_swaps += 1
                    swap(puzzle_list, j, j+1)

        print("\n----------Bubble Sort----------\nComparisons: {};\nSwaps: {}.\n"
              .format(self.number_of_comparisons, self.number_of_swaps))
