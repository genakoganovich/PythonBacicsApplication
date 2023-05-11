def count_replacement(s, a, b, max_count=1000):
    count = 0
    while a in s:
        s = s.replace(a, b)
        count += 1
        if count > max_count:
            return 'Impossible'
    return count


def test():
    import sys
    sys.stdin = open('3.1.1.input.txt', 'r')

    try:
        while True:
            assert str(count_replacement(input(), input(), input())) == input()
    except EOFError:
        return


def run():
    print(count_replacement(input(), input(), input()))


# test()
run()
