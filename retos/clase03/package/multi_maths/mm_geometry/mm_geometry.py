""" Geometry Module file for Multi_Maths Package """
# __doc__ (Geometry Module file for testing modules and packages)

import math

from multi_maths import filters as fil


class MM_Geometry():  # pylint: disable=C0103
    """ MM_Geometry class """

    def __init__(self, lang: object, response: str) -> object:
        """
            Init MM_Geometry() class requirements
        """

        self.response = response
        self.lang = lang
        self.filter = fil._run(lang)

    def circle_area(self, radius: float) -> float:
        """
            Returns circle area calc
        """

        result = math.pi * self.filter.value(radius) ** 2

        if self.response == 'text':
            return self.lang["LANG"]["LANG_GEOM_CA_RESULT"].format(result)

        return result

    def circle_circumference(self, radius: float) -> float:
        """
            Returns circle circumference calc
        """

        result = 2 * math.pi * self.filter.value(radius)

        if self.response == 'text':
            return self.lang["LANG"]["LANG_GEOM_CC_RESULT"].format(result)

        return result

    def triangle_area(self, args: tuple) -> float:
        """
            Returns triangle area calc
        """

        result = (self.filter.value(args[0]) * self.filter.value(args[1])) / 2

        if self.response == 'text':
            return self.lang["LANG"]["LANG_GEOM_TA_RESULT"].format(result)

        return result

    def triangle_perimeter(self, args: tuple) -> float:
        """
            Returns triangle perimeter calc
        """

        result = self.filter.value(args[0]) + self.filter.value(args[1]) + self.filter.value(args[2])  # noqa: E501  # pylint: disable=C0301

        if self.response == 'text':
            return self.lang["LANG"]["LANG_GEOM_TP_RESULT"].format(result)

        return result

    def square_area(self, args: tuple) -> float:
        """
            Returns square area calc
        """

        result = self.filter.value(args[0]) * self.filter.value(args[1])

        if self.response == 'text':
            return self.lang["LANG"]["LANG_GEOM_SA_RESULT"].format(result)

        return result

    def square_perimeter(self, args: tuple) -> float:
        """
            Returns square perimeter calc
        """

        result = self.filter.value(args[0]) * 4

        if self.response == 'text':
            return self.lang["LANG"]["LANG_GEOM_SP_RESULT"].format(result)

        return result

    def rectangle_area(self, args: tuple) -> float:
        """
            Returns rectangle area calc
        """

        result = self.filter.value(args[0]) * self.filter.value(args[1])

        if self.response == 'text':
            return self.lang["LANG"]["LANG_GEOM_RA_RESULT"].format(result)

        return result

    def rectangle_perimeter(self, args: tuple) -> float:
        """
            Returns rectangle perimeter calc
        """

        result = (self.filter.value(args[0]) + self.filter.value(args[1])) * 2

        if self.response == 'text':
            return self.lang["LANG"]["LANG_GEOM_RP_RESULT"].format(result)

        return result

    def parallelogram_area(self, args: tuple) -> float:
        """
            Returns parallelogram area calc
        """

        result = self.filter.value(args[0]) * self.filter.value(args[1])

        if self.response == 'text':
            return self.lang["LANG"]["LANG_GEOM_PA_RESULT"].format(result)

        return result

    def parallelogram_perimeter(self, args: tuple) -> float:
        """
            Returns parallelogram perimeter calc
        """

        result = (self.filter.value(args[0]) + self.filter.value(args[1])) * 2

        if self.response == 'text':
            return self.lang["LANG"]["LANG_GEOM_PP_RESULT"].format(result)

        return result


def _run(lang: object, response='digits') -> object:
    """
        Instancer for MM_Geometry() class
    """

    return MM_Geometry(lang, response)
