import argparse
import random

zero_count = 0
one_count = 0


def main(args):
    global zero_count, one_count
    random_list = [random.choice([0, 1]) for _ in range(args.n)]

    unique_value_count = 0
    is_zero_or_one(random_list[0])
    is_zero_or_one(random_list[-1])

    for i in range(1, len(random_list)-1):
        if random_list[i] != random_list[i-1] and random_list[i] != random_list[i+1]:
            unique_value_count += 1
        is_zero_or_one(random_list[i])

    print(f'zero percentage: {zero_count * 100 / args.n}%')
    print(f'one percentage: {one_count * 100 / args.n}%')
    print(f'duplicated value: {len(random_list) - unique_value_count}')


def is_zero_or_one(value: int):
    global zero_count, one_count
    if value == 0:
        zero_count += 1
    else:
        one_count += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--n", help="List size", type=int, default=1000)

    main(parser.parse_args())
