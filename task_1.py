import argparse
import random

zero_count = 0
one_count = 0


def main(args):
    global zero_count, one_count
    random_list = [random.choice(['0', '1']) for _ in range(args.n)]
    list_as_string = ''.join(x for x in random_list)

    for i in range(1, len(random_list) + 1):
        zero_string = "0" * i
        print(f'{zero_string}: {round(list_as_string.count(zero_string) * 100 / (len(random_list) - i + 1), 2)} %')
        one_string = "1" * i
        print(f'{one_string}: {round(list_as_string.count(one_string) * 100 / (len(random_list) - i + 1), 2)} %')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--n", help="List size", type=int, default=100)

    main(parser.parse_args())
