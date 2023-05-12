import sys, re


def select_z3z(cats):
    return list(filter(lambda x: re.search(r'z.{3}z', x), cats))


def test():
    sys.stdin = open('3.2.3.input.txt', 'r')
    cats = []

    try:
        while True:
            cats.append(input())
    except EOFError:
        print(select_z3z(cats))
        assert select_z3z(cats) == ['zabcz', 'zzxzz']


def run():
    for line in sys.stdin:
        line = line.rstrip()
        if re.search(r'z.{3}z', line):
            print(line)


run()