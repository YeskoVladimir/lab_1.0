import argparse
import math
import random

import numpy as np
import matplotlib.pyplot as plt

FUNCTIONS = {
    'sin(x)': np.sin,
    'cos(x)': np.cos,
    'sqrt(x)': np.sqrt,
    'sqr(x)': np.square
}


def main(args):
    size = args.size
    trial_number = args.n
    function = FUNCTIONS[args.func]
    x_axis = np.linspace(0, size)
    y = np.clip(function(x_axis), 0, size)
    count_in_point = 0
    x_points = []
    y_points = []
    area = np.trapz(y, x_axis)

    for i in range(trial_number):
        x_point = random.uniform(0, size)
        y_point = random.uniform(0, size)
        if function(x_point) >= y_point:
            count_in_point += 1
        x_points.append(x_point)
        y_points.append(y_point)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(0, size)
    plt.fill_between(x_axis, y, facecolor='r', alpha=0.3, color='black', linewidth=1, linestyle='--')
    plt.scatter(x_points, y_points, s=2, edgecolors='red')
    plt.title(label=f'func = {args.func}, trials = {args.n}, '
                    f'S = {round(count_in_point/trial_number * size**2, 4)}, real area = {round(area, 2)}')
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--n", help="Trial number", type=int, default=1000)
    parser.add_argument("--size", help="Square size", type=int, default=3)
    parser.add_argument("--func", help="Figure function", choices=['sin(x)', 'cos(x)', 'sqrt(x)', 'sqr(x)'],
                        default='sin(x)')

    main(parser.parse_args())
