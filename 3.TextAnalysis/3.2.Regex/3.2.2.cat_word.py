import sys, re


def select_cat_word(cats):
    return list(filter(lambda x: re.search(r'\bcat\b', x), cats))


def test():
    sys.stdin = open('3.2.2.input.txt', 'r')
    cats = []

    try:
        while True:
            cats.append(input())
    except EOFError:
        print(select_cat_word(cats))
        assert select_cat_word(cats) == ['cat', 'catapult and cat', '"cat"', '!cat?']


def run():
    for line in sys.stdin:
        line = line.rstrip()
        if re.search(r'\bcat\b', line):
            print(line)


test()


