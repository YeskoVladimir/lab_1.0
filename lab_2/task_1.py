import pandas as pd
from matplotlib import pyplot as plt


def moving_average(data: list, period: int) -> list:
    result = []
    for i in range(period-1, len(data)):
        sum_of_period = sum([data[i-j] for j in range(0, period)])
        result.append(sum_of_period/period)
    return result


def weight_moving_average(data: list, period: int) -> list:
    result = []
    for i in range(period-1, len(data)):
        sum_of_period = sum([(data[i-j] * (period - j)) for j in range(0, period)])
        value = sum_of_period / sum([k for k in range(1, period+1)])
        result.append(value)
    return result


def main():
    alibaba = pd.read_csv("alibaba.csv")
    # amazon = pd.read_csv("amazon.csv")
    # att = pd.read_csv("at&t.csv")
    # mastercard = pd.read_csv("mastercard.csv")
    # visa = pd.read_csv("visa.csv")

    alibaba_x = alibaba.index.values.tolist()
    alibaba_ma = moving_average(alibaba['<CLOSE>'].tolist(), 5)
    alibaba_wma = weight_moving_average(alibaba['<CLOSE>'].tolist(), 10)

    plt.scatter(alibaba_x, alibaba['<CLOSE>'].tolist())
    plt.plot([index for index, _ in enumerate(alibaba_ma)], alibaba_ma, 'r')
    plt.plot([index for index, _ in enumerate(alibaba_wma)], alibaba_wma, 'r')
    plt.xlabel("Дни")
    plt.ylabel("Цена в $")
    plt.show()


if __name__ == "__main__":
    main()
