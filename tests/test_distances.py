import numpy as np
import pytest

from pypkgtest import cosine, euclidean, gower


def test_euclidean():
    a = np.array([0, 0])
    b = np.array([3, 4])
    assert euclidean(a, b) == 5.0


def test_cosine():
    a = np.array([1, 0])
    b = np.array([0, 1])
    assert pytest.approx(cosine(a, b)) == 1.0

    a = np.array([1, 1])
    b = np.array([1, 1])
    assert pytest.approx(cosine(a, b)) == 0.0


def test_gower():
    a = np.array([1, 2])
    b = np.array([3, 5])
    ranges = np.array([2, 3])
    # |1-3|/2 = 1
    # |2-5|/3 = 1
    # mean(1, 1) = 1
    assert gower(a, b, ranges) == 1.0

    a = np.array([1, 1])
    b = np.array([1, 1])
    ranges = np.array([2, 3])
    assert gower(a, b, ranges) == 0.0
