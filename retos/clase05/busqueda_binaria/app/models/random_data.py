""" RamdomData Model for BinarySearchAlgorithms"""
# __doc__ (RamdomData Model file for little data structure app
# testing Binary Search Algorithms)

import random
import functools


class RamdomData():
    """
    Class for Ramdom Data Model

    Arguments:
    lang (object)
    data (list)
    search (int)

    Returns a orderer ramdom list from 3 optional modes.

    >>> random_data = RamdomData()
    >>> random_data.mode = 'sample'
    >>> random_data.amounth = 100
    >>> random_data.max = 999
    >>> data = random_data.get_data
    True

    TODO:
        -

    """

    _mode = 'sample'
    _amounth = 50
    _max = 200

    def __init__(self) -> object:
        """
        Init Function

        Arguments:
        self
        """
        self.random_list = []
        random.shuffle(self.random_list)

    @property
    def mode(self) -> str:
        """
        Property Getter for mode

        Arguments:
        self

        Returns getter of mode for data builder (str)

        >>> self.mode
        'numpy'

        TODO:
            -
        """
        return self._mode

    @mode.setter
    def mode(self, value: str) -> str:
        """
        Function Setter for mode

        Arguments:
        self
        value (str)

        Returns setter for mode to select data builder (str)

        >>> random_data = RamdomData()
        >>> random_data.mode = 'sample'

        TODO:
            -
        """
        self._mode = value

    @property
    def amounth(self) -> int:
        """
        Property Getter for amounth

        Arguments:
        self

        Returns getter of amounth for data builder (str)

        >>> self.amounth
        100

        TODO:
            -
        """
        return self._amounth

    @amounth.setter
    def amounth(self, value: int) -> int:
        """
        Function Setter for amounth

        Arguments:
        self
        value (int)

        Returns setter for amounth to set data builder (str)

        >>> random_data = RamdomData()
        >>> random_data.amounth = 100

        TODO:
            -
        """
        self._amounth = value

    @property
    def max(self) -> int:
        """
        Property Getter for max

        Arguments:
        self

        Returns getter of max for data builder (str)

        >>> self.max
        999

        TODO:
            -
        """
        return self._max

    @max.setter
    def max(self, value: int) -> int:
        """
        Function Setter for max

        Arguments:
        self
        value (int)

        Returns setter for mode to set data builder (str)

        >>> random_data = RamdomData()
        >>> random_data.max = 999

        TODO:
            -
        """
        self._max = value

    @property
    def get_data(self) -> list:  # noqa: E501  # pylint: disable=inconsistent-return-statements
        """
        Property to return data by setted mode

        Arguments:
        self

        Return data by setted mode, returns a list() (list)

        TODO:
            -
        """
        if self._mode == 'sample':
            return self._get_random_sample()
        if self._mode == 'randint':
            return self._get_random_randint()
        if self._mode == 'numpy':
            return self._get_random_numpy()

    def _remove_duplicates_decorator(func: list) -> list:  # noqa: E501  # pylint: disable=no-self-argument
        """
        Decorator for removing duplicated numbers

        Arguments:
        func (list)

        Removes duplicates numbers in list() (list)

        TODO:
            -
        """

        @functools.wraps(func)
        def wrapped_remove_duplicates(self) -> list:
            test_list = func(self)  # pylint: disable=not-callable
            value = []
            [value.append(x) for x in test_list if x not in value]  # noqa: E501  # pylint: disable=expression-not-assigned
            return value
        return wrapped_remove_duplicates

    def _sorted_decorator(func: list) -> list:  # noqa: E501  # pylint: disable=no-self-argument
        """
        Decorator for sorting numbers

        Arguments:
        func (list)

        Order from smallest to largest numbers in list() (list)

        TODO:
            -
        """

        @functools.wraps(func)
        def wrapped_sorted(self) -> list:
            value = func(self)  # pylint: disable=not-callable
            return sorted(value)
        return wrapped_sorted

    @_sorted_decorator
    def _get_random_sample(self) -> list:
        """
        Function to get data from random sample mode

        Arguments:
        self

        Build data numbers with random sample mode, returns a list() (list)

        TODO:
            -
        """
        return random.sample(range(0, self._max), self._amounth)

    @_sorted_decorator
    @_remove_duplicates_decorator
    def _get_random_randint(self) -> list:
        """
        Function to get data from random randint mode

        Arguments:
        self

        Build data numbers with random randint mode, returns a list() (list)

        TODO:
            -
        """
        return list(
            random.randint(1, self._max) for _ in range(0, self._amounth))

    @_sorted_decorator
    @_remove_duplicates_decorator
    def _get_random_numpy(self) -> list:
        """
        Function to get data from numpy`s random randint mode

        Arguments:
        self

        Build data numbers with numpy`s random randint mode, returns a
        list() (list)

        TODO:
            -
        """
        import numpy as np  # pylint: disable=import-outside-toplevel
        return np.random.randint(0, high=self._max, size=self._amounth,
                                 dtype=int).tolist()
