import sys, re


def swap_two_first(cats):
    return list(map(lambda x: re.sub(r'\b(\w)(\w)((\w)*)\b', r'\2\1\3', x), cats))


def test():
    sys.stdin = open('3.2.8.input.txt', 'r')
    cats = []

    try:
        while True:
            cats.append(input())
    except EOFError:
        print(swap_two_first(cats))
        assert swap_two_first(cats) == ['htis si a etxt', '"htis\' !si. ?1nce,']


def run():
    for line in sys.stdin:
        line = line.rstrip()
        print(re.sub(r'\b(\w)(\w)((\w)*)\b', r'\2\1\3', line))

