class Puzzle:

    def __init__(self, description, number_of_elements, packaging_width, packaging_height):
        self.description = description
        self.number_of_elements = int(number_of_elements)
        self.packaging_width = int(packaging_width)
        self.packaging_height = int(packaging_height)

    def __repr__(self):
        return "Description: {}; Number of Elements: {}; Packaging width: {}; Packaging height: {}.\n"\
            .format(self.description, self.number_of_elements, self.packaging_width, self.packaging_height)
