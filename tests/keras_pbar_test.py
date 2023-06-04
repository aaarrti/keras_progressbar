import pytest

from keras_pbar import keras_pbar


def test_list_of_ints():
    int_list = range(10)
    for i in keras_pbar(int_list):
        assert isinstance(i, int)


def test_not_sized_fails():
    r = map(str, range(10))
    with pytest.raises(ValueError):
        for _ in keras_pbar(r):
            pass


def test_not_sized():
    def gen():
        for i in range(10):
            yield 0

    for i in keras_pbar(gen(), n=10):
        assert i == 0


def test_enumerate():
    el = range(10)
    for i, j in enumerate(keras_pbar(el)):
        assert i == j


def test_zip():
    l1 = [1, 2, 3, 4, 5]
    l2 = [-1, -2, -3, -4, -5]

    for i, j in keras_pbar(zip(l1, l2), n=5):
        assert i == -j
