#!/usr/bin/python3


def addComplex(x, y):
    # add code here ...
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]
    return (a + c, b + d)


def multiplyComplex(x, y):
    # addapt code to use named tuples
    pass


def printComplex(x):
    # addapt code to use named tuples
    pass


def main():
    # define two complex numbers as tuples of size two
    c1 = (3,5)
    c2 = (7,1)
    c3 = (3,4)
    addComplex(c1, c2)

if __name__ == '__main__':
    main()