class Fraction:
    __nominator = None
    __denominator = None

    def __init__(self, nominator, denominator):
        self.__nominator = nominator
        self.__denominator = denominator

    def __str__(self):
        ret_val = ""
        ret_val = ret_val + str(self.__nominator) + " " + str(self.__denominator)
        return ret_val

    def __add__(self, other):
        common_denominator = self.__denominator * other.__denominator
        first_nominator = (common_denominator / self.__denominator) * self.__nominator
        second_nominator = (common_denominator / other.__denominator) * other.__nominator
        ret_val = Fraction(int(first_nominator + second_nominator), common_denominator)
        return ret_val

    def __sub__(self, other):
        common_denominator = self.__denominator * other.__denominator
        first_nominator = (common_denominator / self.__denominator) * self.__nominator
        second_nominator = (common_denominator / other.__denominator) * other.__nominator
        ret_val = Fraction(int(first_nominator - second_nominator), common_denominator)
        return ret_val

    def inverse(self):
        new_nominator = self.__denominator
        new_denominator = self.__nominator
        ret_val = Fraction(new_nominator, new_denominator)
        return ret_val


def exec_lesson_5():
    first_fraction = Fraction(1, 2)
    second_fraction = Fraction(2, 3)
    third_fraction = first_fraction - second_fraction
    fourth_fraction = second_fraction.inverse()
    print(third_fraction)
    print(fourth_fraction)
