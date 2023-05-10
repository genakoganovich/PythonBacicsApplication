def redirect_stdin():
    sys = __import__('sys')
    sys.stdin = open("input.txt", "r")


redirect_stdin()