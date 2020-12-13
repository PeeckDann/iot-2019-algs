def read(file_name):
    with open(file_name, "r+") as file:
        number_of_words = int(file.readline())
        words = []
        for line in file:
            words.append(line.replace("\n", ""))

    return words
