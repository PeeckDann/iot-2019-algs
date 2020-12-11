from manager.word_counter import count, final_count

if __name__ == '__main__':
    with open("wchain3.in", "r+") as file:
        number_of_words = int(file.readline())
        words = []
        for line in file:
            words.append(line.replace("\n", ""))

    with open("wchain.out", "w") as file:
        file.write(f'{final_count(words)}')
