def swap(puzzle_list, first_element, second_element):
    temporary = puzzle_list[first_element]
    puzzle_list[first_element] = puzzle_list[second_element]
    puzzle_list[second_element] = temporary
