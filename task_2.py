import argparse
import random

import numpy as np
import matplotlib.pyplot as plt


def main(args):
    list_length = random.randint(1, args.max_length)
    random_list = [random.uniform(args.range_min, args.range_max) for _ in range(list_length)]

    mean = sum(random_list) / len(random_list)
    std = np.std(random_list)
    x_axis = [i for i in range(list_length)]
    a, b = np.linalg.lstsq(np.vstack([x_axis, np.ones(len(x_axis))]).T, random_list, rcond=None)[0]
    y_axis = [a * x + b for x in x_axis]

    print(f'Массив: {random_list}')
    print(f'Длина массива : {list_length}')
    print(f'Математическое ожидание: {mean}')
    print(f'Cреднеквадратическое отклонение: {std}')

    plt.plot(x_axis, y_axis)
    plt.scatter(x_axis, random_list)
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--max-length", type=int, default=30)
    parser.add_argument("--range-min", type=float, default=-100)
    parser.add_argument("--range-max", type=float, default=100)

    main(parser.parse_args())
