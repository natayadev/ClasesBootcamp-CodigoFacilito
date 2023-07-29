""" Algorithms Binary Model for BinarySearchAlgorithms"""
# __doc__ (Algorithms Binary Model file for little data structure app
# testing Binary Search Algorithms)


class AlgorithmBinarySearch():  # pylint: disable=too-few-public-methods
    """
    Class for Algorithm Binary Search Model

    Arguments:
    lang (object)
    data (list)
    search (int)

    Returns a Binary Search from a list of numbers.

    >>> binary_search = AlgorithmBinarySearch()
    >>> binary_search.get(lang, data, search_value)
    True

    TODO:
        -

    """

    @classmethod
    def get(cls, lang: object, data: list, search: int) -> str:
        """
        Class-Method to return by binary search algorithm

        Arguments:
        cls
        lang (object)
        data (list)
        search (int)

        Returns a seach from list() using binary search algorithm (str)

        TODO:
            -
        """
        start = 0
        end = len(data) - 1
        half = (start+end)//2
        element = data[half]
        search = int(search)

        while start <= end:

            if data[half] == search:
                return lang["LANG"]["LANG_MODELS_ALG_BIN_INDEX"].format(
                    search, half)

            if data[half] < search:
                start = half + 1
                end = len(data) - 1
                half = (start + end) // 2
                element = data[half]
                if element == search:
                    return lang["LANG"]["LANG_MODELS_ALG_BIN_INDEX"].format(
                        element, half)

            if data[half] > search:
                end = half - 1
                half = (start + end) // 2
                element = data[half]
                if element == search:
                    return lang["LANG"]["LANG_MODELS_ALG_BIN_INDEX"].format(
                        element, half)

        return lang["LANG"]["LANG_MODELS_ALG_BIN_NOT_IN_LIST"].format(search)
