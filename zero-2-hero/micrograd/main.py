import math
import numpy as np
import matplotlib.pyplot as plt
import plotext as pltx


def f(x):
    return 3*x**2 - 4*x +5


def main():
    print(f(3.0))

    xs = np.arange(-5, 5, 0.25)
    ys = f(xs)

    pltx.plot(xs, ys)
    pltx.show()


if __name__ == "__main__":
    main()