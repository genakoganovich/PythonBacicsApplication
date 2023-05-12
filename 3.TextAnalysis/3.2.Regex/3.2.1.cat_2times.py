import re, sys


def select_cats(cats):
    return list(filter(lambda x: len(re.findall(r'cat', x)) >= 2, cats))


def test():
    sys.stdin = open('3.2.1.input.txt', 'r')
    cats = []

    try:
        while True:
            cats.append(input())
    except EOFError:
        assert select_cats(cats) == ['catcat', 'cat and cat']


def run():
    for line in sys.stdin:
        line = line.rstrip()
        if len(re.findall(r'cat', line)) >= 2:
            print(line)


run()