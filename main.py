from manager.experience_counter import count, create_graph


if __name__ == '__main__':
    with open("career(0).in", "r+") as file:
        levels = int(file.readline())
        node_values = []
        for line in file:
            values = line.split()
            for i in values:
                node_values.append(int(i))

    with open("career.out", "w") as file:
        file.write(f'{count(create_graph(levels), node_values, levels)}')
