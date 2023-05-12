import sys, re


def remove_double(cats):
    return list(map(lambda x: re.sub(r'(\w)(\1)+', r'\1', x), cats))


def test():
    sys.stdin = open('3.2.9.input.txt', 'r')
    cats = []

    try:
        while True:
            cats.append(input())
    except EOFError:
        print(remove_double(cats))
        assert remove_double(cats) == ['atraction', 'buz']


def run():
    for line in sys.stdin:
        line = line.rstrip()
        print(re.sub(r'(\w)(\1)+', r'\1', line))
