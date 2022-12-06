import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA


def main():
    data = pd.read_csv("lab_2_2.csv")
    x = StandardScaler().fit_transform(data.T)
    pca = PCA()
    principal_components = pca.fit_transform(x)

    per_var = np.round(pca.explained_variance_ratio_ * 100, decimals=1)
    labels = ['PC' + str(x) for x in range(1, len(per_var) + 1)]

    principal_dataframe = pd.DataFrame(principal_components, index=data.columns.tolist(), columns=labels)

    plt.scatter(principal_dataframe.PC1, principal_dataframe.PC2)
    plt.title('My PCA Graph')
    plt.xlabel(f'PC1 - {per_var[0]}%')
    plt.ylabel(f'PC2 - {per_var[1]}%')

    for sample in principal_dataframe.index:
        plt.annotate(sample, (principal_dataframe.PC1.loc[sample], principal_dataframe.PC2.loc[sample]))

    plt.show()


if __name__ == "__main__":
    main()
