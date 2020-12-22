from manager.rabin_karp import find_matches
from utils.read import read

if __name__ == '__main__':
    prime_number = 101
    text, pattern = read("input1.txt")
    result = str(find_matches(text, pattern, prime_number)).replace("[", "").replace("]", "")
    with open("output.txt", "w") as file:
        file.write(f'Found matches at indexes {result}')
