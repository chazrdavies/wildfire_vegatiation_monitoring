import numpy as np

# functions for normalizing data


NAN_VALUE = -9999


def norm_vis(arr, p2, p98):
    arr = np.clip(arr, p2, p98)

    return (arr - p2) / (p98 - p2 + 1e-8)

def min_max_normalize(arr: np.ndarray) -> np.ndarray:
    arr = np.where(arr == NAN_VALUE, np.nan, arr)
    return (arr - np.nanmin(arr)) / (np.nanmax(arr) - np.nanmin(arr))
