import numpy as np


def pearson_cor(x, y):
    """ Copied from https://cancerdatascience.org/blog/posts/pearson-correlation/ """
    xv = x - x.mean(axis=0)
    yv = y - y.mean(axis=0)
    xvss = (xv * xv).sum(axis=0)
    yvss = (yv * yv).sum(axis=0)
    result = np.matmul(xv.transpose(), yv) / np.sqrt(np.outer(xvss, yvss))
    # bound the values to -1 to 1 in the event of precision issues
    return np.maximum(np.minimum(result, 1.0), -1.0)


def find_max_correlation(input_series, all_series):
    correlations = pearson_cor(input_series.transpose(), all_series.transpose())
    max_correlation_idx = int(abs(correlations).argmax(axis=1))
    max_correlation = correlations[0, max_correlation_idx]

    return max_correlation, max_correlation_idx
