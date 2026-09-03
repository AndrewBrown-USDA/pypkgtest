import numpy as np


def euclidean(a: np.ndarray, b: np.ndarray) -> float:
    """
    Calculate the Euclidean distance between two arrays.

    Args:
        a: First array.
        b: Second array.

    Returns:
        The Euclidean distance between a and b.
    """
    return float(np.linalg.norm(a - b))


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    """
    Calculate the cosine distance between two arrays.

    Args:
        a: First array.
        b: Second array.

    Returns:
        The cosine distance between a and b.
    """
    return float(1 - np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def gower(a: np.ndarray, b: np.ndarray, ranges: np.ndarray) -> float:
    """
    Calculate the Gower distance between two arrays for numeric features.

    Args:
        a: First array.
        b: Second array.
        ranges: The range (max - min) for each feature.

    Returns:
        The Gower distance between a and b.
    """
    return float(np.mean(np.abs(a - b) / ranges))
