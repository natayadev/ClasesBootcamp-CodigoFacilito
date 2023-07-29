""" Arithmetic Module file for Multi_Maths Package """
# __doc__ (Arithmetic Module file for testing modules and packages)

from multi_maths import filters as fil


class MM_Arithmetic():  # pylint: disable=C0103
    """ MM_Arithmetic class """

    def __init__(self, lang: object, response: str) -> object:
        """
            Init MM_Arithmetic() class requirements
        """

        self.response = response
        self.lang = lang
        self.filter = fil._run(lang)

    def addition(self, args: tuple) -> float:
        """
            Returns addition calc
        """

        result = None
        for num in args:
            if result is None:
                result = self.filter.value(num)
            else:
                result = result + self.filter.value(num)

        if self.response == 'text':
            return self.lang["LANG"]["LANG_ARITH_ADD_RESULT"].format(result)

        return result

    def subtraction(self, args: tuple) -> float:
        """
            Returns subtraction calc
        """

        result = None
        for num in args:
            if result is None:
                result = self.filter.value(num)
            else:
                result = result - self.filter.value(num)

        if self.response == 'text':
            return self.lang["LANG"]["LANG_ARITH_SUB_RESULT"].format(result)

        return result

    def multiplication(self, args: tuple) -> float:
        """
            Returns multiplication calc
        """

        result = None
        for num in args:
            if result is None:
                result = self.filter.value(num)
            else:
                result = result * self.filter.value(num)

        if self.response == 'text':
            return self.lang["LANG"]["LANG_ARITH_MUL_RESULT"].format(result)

        return result

    def division(self, args: tuple) -> float:
        """
            Returns division calc
        """

        result = None
        for num in args:
            if self.filter.value(num) != 0:
                if result is None:
                    result = self.filter.value(num)
                else:
                    result = result / self.filter.value(num)
            else:
                return self.lang["LANG"]["LANG_ARITH_DIV_BY_ZERO_ERROR"]

        if self.response == 'text':
            return self.lang["LANG"]["LANG_ARITH_DIV_RESULT"].format(result)

        return result

    def modulus(self, args: tuple) -> float:
        """
            Returns modulus calc
        """

        result = (self.filter.value(args[0]
                                    ) * self.filter.value(args[1])) / 100

        if self.response == 'text':
            return self.lang["LANG"]["LANG_ARITH_MOD_RESULT"].format(result)

        return result

    def exponentiation(self, args: tuple) -> float:
        """
            Returns exponentiation calc
        """

        result = self.filter.value(args[0]) ** self.filter.value(args[1])

        if self.response == 'text':
            return self.lang["LANG"]["LANG_ARITH_EXP_RESULT"].format(result)

        return result

    def floor_division(self, args: tuple) -> float:
        """
            Returns floor division calc
        """

        check1 = self.filter.value(args[0])
        check2 = self.filter.value(args[1])
        if check1 != 0 and check2 != 0:
            result = self.filter.value(args[0]) // self.filter.value(args[1])
        else:
            return self.lang["LANG"]["LANG_ARITH_DIV_BY_ZERO_ERROR"]

        if self.response == 'text':
            return self.lang["LANG"]["LANG_ARITH_FDIV_RESULT"].format(result)

        return result


def _run(lang: object, response='digits') -> object:
    """
        Instancer for MM_Arithmetic() class
    """

    return MM_Arithmetic(lang, response)
