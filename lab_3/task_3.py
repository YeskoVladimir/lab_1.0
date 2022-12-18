import itertools
import random

from matplotlib import pyplot as plt


class Deck:
    deck = list(itertools.product(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
                                  ['Spade', 'Heart', 'Diamond', 'Club']))

    def __iter__(self):
        return self.deck

    def __getitem__(self, item):
        return self.deck[item]

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def sort(self, order: None | str = None) -> list:
        if not order:
            return sorted(self.deck)
        elif order == 'face':
            return sorted(self.deck, key=lambda x: x[0])
        elif order == 'suit':
            return sorted(self.deck, key=lambda x: x[1])

    def remove_card(self, card: int | tuple[str, str] | None):
        if not card:
            self.deck.pop()
        elif isinstance(card, tuple):
            self.deck.remove(card)
        elif isinstance(card, int):
            self.deck.pop(card)


def main():
    trial_powers = [i for i in range(1, 7)]
    real_value = 4 / 52 * 3 / 51
    deck = Deck()
    x = []
    y = []
    y_real = [real_value] * 6

    for trial_power in trial_powers:
        double_aces = 0
        trial = 10 ** trial_power
        for hands in range(trial):
            deck.shuffle()
            aces = [d[0] for d in deck[0:2]].count('A')
            if aces == 2:
                double_aces += 1
        prob = double_aces / trial
        x.append(trial_power)
        y.append(prob)

    plt.xlabel("Trials = 10^x")
    plt.ylabel("Probability")
    plt.title(f"Real probability = {round(real_value, 3)}, Monte Carlo probability = {round(y[-1], 3)}")
    plt.plot(x, y)
    plt.plot(x, y_real)
    plt.show()


if __name__ == "__main__":
    main()
