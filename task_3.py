import random
import pandas as pd
from matplotlib import pyplot as plt
from pandas import Series


def main():
    mas_vis = pd.read_csv("mas_vis.csv")
    corr_matrix = mas_vis.corr(method='pearson')
    coef = corr_matrix.MAS.VIS

    values_initial = mas_vis.MAS
    indexes_to_delete = random.sample(range(1, len(values_initial) - 2), 100)
    indexes_to_delete.sort()

    values_nulled = mas_vis.MAS.copy()
    for index in indexes_to_delete:
        values_nulled[index] = 0
    values_winsorized = winsorize(values_nulled)
    values_approx = lin_approximation(values_nulled)
    values_correlated = correlation(values_nulled, mas_vis.VIS, coef, nulled_count=len(indexes_to_delete))

    frame = {
        'Modified': values_nulled,
        'Initial': values_initial,
        'Winsorization': values_winsorized,
        'Linear Approximation': values_approx,
        'Correlation': values_correlated,
    }
    result = pd.DataFrame(frame)
    result.to_csv('task_3.csv')

    x_axis = [i for i in range(len(values_initial))]
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(x_axis, values_initial)
    axs[0, 0].set_title("Исходный")
    axs[1, 0].plot(x_axis, values_winsorized)
    axs[1, 0].set_title("Винзорирование")
    axs[1, 0].sharex(axs[0, 0])
    axs[0, 1].plot(x_axis, values_approx)
    axs[0, 1].set_title("Линейное приб")
    axs[1, 1].plot(x_axis, values_correlated)
    axs[1, 1].set_title("Корреляция")
    fig.tight_layout()
    fig.show()

def winsorize(values: Series) -> Series:
    values_winsorized = values.copy()
    for i in range(len(values_winsorized)):
        if values_winsorized[i] == 0:
            for j in range(i-1, 0, -1):
                if values_winsorized[j] != 0:
                    values_winsorized[i] = values_winsorized[j]
                    break
            if values_winsorized[i] == 0:
                for j in range(i+1, len(values_winsorized)):
                    if values_winsorized[j] != 0:
                        values_winsorized[i] = values_winsorized[j]
                        break
    return values_winsorized


def lin_approximation(values: Series) -> Series:
    values_approx = values.copy()

    empty_values = 0
    first_value = 0
    for i in range(len(values_approx)):
        if values_approx[i] == 0:
            if empty_values == 0:
                first_value = values_approx[i-1]
            empty_values += 1
        else:
            if empty_values != 0:
                second_value = values_approx[i]
                step = (second_value - first_value) / (empty_values + 1)
                for j in range(i-1, i-empty_values-1, -1):
                    values_approx[j] = values_approx[j+1] - step
            empty_values = 0
    return values_approx


def correlation(values_nulled: Series, values_related: Series, coef: float, nulled_count: int) -> Series:
    values_correlated = values_nulled.copy()
    mean_related = sum(values_related) / len(values_related)
    mean_nulled = sum(values_nulled) / (len(values_nulled) - nulled_count)

    for i in range(len(values_correlated)):
        if values_correlated[i] == 0:
            values_correlated[i] = mean_nulled + (values_related[i] - mean_related) * coef / abs(coef)

    return values_correlated


if __name__ == "__main__":
    main()
