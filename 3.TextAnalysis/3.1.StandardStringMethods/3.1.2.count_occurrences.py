def solution_1():
    s, t = input(), input()
    print(sum(1 for i in range(len(s)) if s.startswith(t, i)))


def solution_2():
    import re
    s, t = input(), '(?=' + input() + ')'
    print(len(re.findall(t, s)))


def solution_3():
    s, t = input(), input()
    print(len(list(filter(lambda x: x == t, (s[i: i + len(t)] for i in range(len(s) - len(t) + 1))))))


def solution_4():
    s, t = input(), input()
    print(len(list(filter(lambda i: s.startswith(t, i), range(len(s))))))


def count_occurrences_start(s, t):
    count = 0
    for i in range(len(s)):
        if str(s).startswith(t, i):
            count += 1
    return count


def count_occurrences(s, t):
    count = 0
    pos = s.find(t)
    while pos != -1:
        count += 1
        pos += 1
        pos = s.find(t, pos)

    return count


def test():
    import sys
    sys.stdin = open('3.1.2.input.txt', 'r')

    try:
        while True:
            assert str(count_occurrences_start(input(), input())) == input()

    except EOFError:
        return


def run():
    print(count_occurrences(input(), input()))


# run()
test()
