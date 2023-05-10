def foo():
    pass


if __name__ == "__main__":
    try:
        foo()
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except ArithmeticError:
        print("ArithmeticError")
    except AssertionError:
        print("AssertionError")
