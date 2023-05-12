import sys, re


def replace_first_ignore(cats):
    return list(map(lambda x: re.sub(r'\ba+\b', 'argh', x, count=1, flags=re.IGNORECASE), cats))


def test():
    sys.stdin = open('3.2.7.input.txt', 'r')
    cats = []

    try:
        while True:
            cats.append(input())
    except EOFError:
        print(replace_first_ignore(cats))
        # assert replace_first_ignore(cats) == ['There’ll be no more "argh"', 'argh AaAaAaA']


def run():
    for line in sys.stdin:
        line = line.rstrip()
        print(re.sub(r'\ba+\b', 'argh', line, count=1, flags=re.IGNORECASE))
