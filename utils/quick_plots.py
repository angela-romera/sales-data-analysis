import matplotlib.pyplot as plt
import seaborn as sns


def boxplot_per_column(df):
    num_columns = df.shape[1]
    fig, axes = plt.subplots(nrows=1, ncols=num_columns, figsize=(2 * num_columns, 6))
    for i, col in enumerate(df.columns):
        sns.boxplot(y=df[col], ax=axes[i])
        axes[i].set_title(col)
        axes[i].set_ylabel('')

    plt.tight_layout()
    plt.show()


def histogram_per_column(df):
    num_columns = df.shape[1]
    fig, axes = plt.subplots(nrows=1, ncols=num_columns, figsize=(2 * num_columns, 6))
    for i, col in enumerate(df.columns):
        sns.histplot(df[col], ax=axes[i], bins=6, discrete=True, stat='count')
        axes[i].set_title(col)
        axes[i].set_ylabel('')

    plt.tight_layout()
    plt.show()


def barplot_two_vars(df, x_var, y_var):
    sns.barplot(data=df, x=x_var, y=y_var, estimator="sum", errorbar=None)

    plt.xlabel(x_var)
    plt.ylabel(y_var)

    plt.show()
