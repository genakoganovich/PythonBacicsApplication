import sys, re


def select_back_slash(cats):
    return list(filter(lambda x: re.search(r'\\', x), cats))


def test():
    sys.stdin = open('3.2.4.input.txt', 'r')
    cats = []

    try:
        while True:
            cats.append(input())
    except EOFError:
        print(select_back_slash(cats))
        # assert select_back_slash(cats) == ['zabcz', r'\w denotes word character']


def run():
    for line in sys.stdin:
        line = line.rstrip()
        if re.search(r'\\', line):
            print(line)


