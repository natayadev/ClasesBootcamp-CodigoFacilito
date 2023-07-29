""" Statistics Module file for Multi_Maths Package """
# __doc__ (Statistics Module file for testing modules and packages)

import statistics


class MM_Statistics():  # pylint: disable=C0103
    """ MM_Statistics class """

    def __init__(self, lang: object, response: str) -> object:
        """
            Init MM_Statistics() class requirements
        """
        self.response = response
        self.lang = lang

    def standard_deviation(self, data_list: list, xbar=0) -> float:
        """
            Returns standard deviation calc
        """

        if xbar != 0:
            result = statistics.stdev(data_list, xbar)
        else:
            result = statistics.stdev(data_list)

        if self.response == 'text':
            return self.lang["LANG"]["LANG_STAT_STDEV_RESULT"].format(result)

        return result

    def mean(self, data_list: list) -> float:
        """
            Returns mean calc
        """

        result = statistics.mean(data_list)

        if self.response == 'text':
            return self.lang["LANG"]["LANG_STAT_MEAN_RESULT"].format(result)

        return result

    def median(self, data_list: list) -> float:
        """
            Returns median calc
        """

        result = statistics.median(data_list)

        if self.response == 'text':
            return self.lang["LANG"]["LANG_STAT_MEDI_RESULT"].format(result)

        return result

    def mode(self, data_list: list) -> float:
        """
            Returns mode calc
        """

        result = statistics.mode(data_list)

        if self.response == 'text':
            return self.lang["LANG"]["LANG_STAT_MODE_RESULT"].format(result)

        return result


def _run(lang: object, data_list: list, xbar=0) -> object:
    """
        Instancer for MM_Statistics() class
    """

    return MM_Statistics(lang, data_list, xbar)  # pylint: disable=E1121
