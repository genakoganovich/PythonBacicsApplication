import sys, re


def select_tandem_word(cats):
    return list(filter(lambda x: re.search(r'\b(\w+)\1\b', x), cats))


def test():
    sys.stdin = open('3.2.5.input.txt', 'r')
    cats = []

    try:
        while True:
            cats.append(input())
    except EOFError:
        print(select_tandem_word(cats))
        assert select_tandem_word(cats) == ['blabla is a tandem repetition', '123123 is good too']


def run():
    for line in sys.stdin:
        line = line.rstrip()
        if re.search(r'\b(\w+)\1\b', line):
            print(line)
