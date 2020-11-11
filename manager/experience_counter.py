def count_nodes(level_num):
    """
    >>> count_nodes(4)
    10
    >>> count_nodes(3)
    6
    >>> count_nodes(2)
    3
    """
    return round(((1 + level_num) / 2) * level_num)


def create_graph(level_num):
    """
    >>> create_graph(4)
    {0: [1, 2], 1: [3, 4], 2: [4, 5], 3: [6, 7], 4: [7, 8], 5: [8, 9], 6: [], 7: [], 8: [], 9: []}
    >>> create_graph(3)
    {0: [1, 2], 1: [3, 4], 2: [4, 5], 3: [], 4: [], 5: []}
    >>> create_graph(2)
    {0: [1, 2], 1: [], 2: []}
    """
    graph = {}
    node_num = 1

    for i in range(0, level_num):
        for j in range(0, node_num):
            k = count_nodes(i)
            if node_num == level_num:
                graph[k + j] = []
            else:
                graph[k + j] = [k + node_num + j, k + node_num + j + 1]
        node_num += 1

    return graph


def has_key(graph, target_node):
    """
    >>> has_key({0: [1, 2], 1: [3, 4], 2: [4, 5], 3: [], 4: [], 5: []}, 1)
    True
    >>> has_key({0: [1, 2], 1: [3, 4], 2: [4, 5], 3: [], 4: [], 5: []}, 9)
    False
    """
    nodes = list(graph.keys())
    for node in nodes:
        if node == target_node:
            return True
    return False


def find_all_paths(graph, start, end, path=[]):
    """
    >>> find_all_paths({0: [1, 2], 1: [3, 4], 2: [4, 5], 3: [], 4: [], 5: []}, 0, 4)
    [[0, 1, 4], [0, 2, 4]]
    >>> find_all_paths({0: [1, 2], 1: [3, 4], 2: [4, 5], 3: [], 4: [], 5: []}, 0, 3)
    [[0, 1, 3]]
    """
    if not has_key(graph, start):
        return []

    path = path + [start]
    if start == end:
        return [path]

    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


def count(graph, nodes_values, level_num):
    """
    >>> count({0: [1, 2], 1: [3, 4], 2: [4, 5], 3: [], 4: [], 5: []}, [4, 3, 1, 2, 1, 5], 3)
    10
    """
    end_nodes = []
    biggest_experience = 0
    for i in range(0, count_nodes(level_num)):
        if not graph[i]:
            end_nodes.append(i)
    for i in end_nodes:
        for j in find_all_paths(graph, 0, i):
            experience = 0
            for k in j:
                experience += nodes_values[k]
            if experience > biggest_experience:
                biggest_experience = experience
    return biggest_experience


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
