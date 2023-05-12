import sys, re


def select_binary_mult3(cats):
    return list(filter(lambda x:
                       re.match(r'^((((0+)?1)(10*1)*0)(0(10*1)*0|1)*(0(10*1)*(1(0+)?))|(((0+)?1)(10*1)*(1('
                                r'0+)?)|(0(0+)?)))$', x), cats))


def test():
    sys.stdin = open('3.2.10.input.txt', 'r')
    cats = []

    try:
        while True:
            cats.append(input())
    except EOFError:
        print(select_binary_mult3(cats))
        assert select_binary_mult3(cats) == ['0', '10010', '01001']


def run():
    for line in sys.stdin:
        line = line.rstrip()
        if re.match(r'^((((0+)?1)(10*1)*0)(0(10*1)*0|1)*(0(10*1)*(1(0+)?))|(((0+)?1)(10*1)*(1('
                    r'0+)?)|(0(0+)?)))$', line):
            print(line)
