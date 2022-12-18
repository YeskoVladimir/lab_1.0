import argparse

import matplotlib.pyplot as plt
import random


def roll_dice():
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)

    if die_1 == die_2:
        same_num = True
    else:
        same_num = False
    return same_num


def main(args):
    trial_number = args.n
    bet = args.bet
    rolls = args.rolls
    start_balance = args.balance
    coef = args.coef

    win_probability = []
    end_balance = []
    
    plt.xlabel("Roll Number")
    plt.ylabel("Balance [$]")
    plt.xlim([0, rolls])
    
    for i in range(trial_number):
        balance = [start_balance]
        num_rolls = [0]
        num_wins = 0

        while num_rolls[-1] < rolls:
            same = roll_dice()

            if same:
                balance.append(balance[-1] + (coef-1) * bet)
                num_wins += 1
            else:
                balance.append(balance[-1] - bet)
    
            num_rolls.append(num_rolls[-1] + 1)

        win_probability.append(num_wins/num_rolls[-1])
        end_balance.append(balance[-1])
        plt.plot(num_rolls, balance)

    overall_win_probability = sum(win_probability) / len(win_probability)
    overall_end_balance = sum(end_balance) / len(end_balance)
    plt.title(f"Trials = {trial_number}, avg_win = {overall_win_probability}, "
              f"avg_total_balance = {overall_end_balance}, coef = {coef}, bet = {bet}")
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--n", help="Trial number", type=int, default=1000)
    parser.add_argument("--bet", help="Bet size", type=int, default=1)
    parser.add_argument("--rolls", help="Number of rolls", type=int, default=300)
    parser.add_argument("--balance", help="Start balance", type=int, default=100)
    parser.add_argument("--coef", help="Win coefficient", type=int, default=6)

    main(parser.parse_args())
