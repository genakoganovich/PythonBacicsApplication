import json
import sys


def build_parents_dict(json_to_python):
    result = {}
    for item in json_to_python:
        result[item['name']] = item['parents']
    return result


def is_parent(child, parent, parents_d):
    return child == parent or any(map(lambda p: is_parent(p, parent, parents_d), parents_d[child]))


def calculate_ancestors(parent, parents_d):
    count = 0
    for child in parents_d.keys():
        if is_parent(child, parent, parents_d):
            count += 1
    return count


def test():
    sys.stdin = open('3.4.2.input.txt', 'r')
    for line in sys.stdin:
        parents_dict = build_parents_dict(json.loads(line))
        sorted_keys = sorted(parents_dict.keys())
        for parent in sorted_keys:
            print(f'{parent} : {calculate_ancestors(parent, parents_dict)}')

        print()


def run():
    data_json = input()
    parents_dict = build_parents_dict(json.loads(data_json))
    sorted_keys = sorted(parents_dict.keys())
    for parent in sorted_keys:
        print(f'{parent} : {calculate_ancestors(parent, parents_dict)}')


run()
