import sys, re


def replace_human_comp(cats):
    return list(map(lambda x: re.sub('human', 'computer', x), cats))


def test():
    sys.stdin = open('3.2.6.input.txt', 'r')
    cats = []

    try:
        while True:
            cats.append(input())
    except EOFError:
        print(replace_human_comp(cats))
        assert replace_human_comp(cats) == ['I need to understand the computer mind', 'computerity']


def run():
    for line in sys.stdin:
        line = line.rstrip()
        print(re.sub('human', 'computer', line))
