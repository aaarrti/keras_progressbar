from __future__ import annotations

from typing import Sized, Iterable, TypeVar
from keras.utils import Progbar

T = TypeVar("T")


def keras_pbar(iterable: Iterable[T], n: int | None = None) -> Iterable[T]:
    """
    Prints Keras progress bar to stdout and updates it on every iteration.

    Parameters
    ----------
    iterable:
        The iterable for which progress bar should be displayed.
    n:
        If iterable is not sized, must explicitly provide the length.

    Returns
    -------

    it:
        Iterable, which updates progress bar on every step.


    Examples
    -------
    >>> import time
    >>> import pandas as pd
    >>> from keras_pbar import keras_pbar
    >>> df = pd.read_csv("data.csv")
    >>> for identifier, sliced in keras_pbar(df.group_by("id")):
    >>>     # Do some time consuming processing.
    >>>     time.sleep(2)

    """
    if n is None:
        if not isinstance(iterable, Sized):
            raise ValueError("Must provide n, for not sized iterable.")
        n = len(iterable)

    pbar = Progbar(n)
    for i in iterable:
        pbar.add(1)
        yield i
