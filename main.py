from manager.word_counter import final_count
from utils.read import read

if __name__ == '__main__':
    with open("wchain.out", "w") as file:
        file.write(f'{final_count(sorted(read("wchain1.in"), key=len), {})}')
