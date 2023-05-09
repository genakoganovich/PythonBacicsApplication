import sys

# sys.stdin = open("input.txt", "r")


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path
    return None


def make_graph(keys_total):
    graph = {}
    for i in range(keys_total):
        key, *value = input().replace(":", " ").split()
        if key not in graph:
            graph[key] = value
        else:
            list(graph[key]).extend(value)
    return graph


def run():
    graph = make_graph(int(input()))
    for i in range(int(input())):
        end, beg = input().split()
        print(get_answer(find_path(graph, beg, end)))


def get_answer(found):
    return 'Yes' if found else 'No'


if __name__ == "__main__":
    run()
