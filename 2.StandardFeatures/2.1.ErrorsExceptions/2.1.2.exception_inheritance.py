import sys

sys.stdin = open("input.txt", "r")


n = int(input())
parents = {}
for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]


def is_parent(child, parent):
    return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))


q = int(input())
exceptions = []
for _ in range(q):
    b = input()
    if any(is_parent(b, a) for a in exceptions):
        print(b)
    else:
        exceptions.append(b)
