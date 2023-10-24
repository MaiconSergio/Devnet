def square_list(number):
    """ Esta função eleva ao quadrado cada número da lista.
    :param numbers: Lista de números a serem elevados ao quadrado.
    :return: Lista de números quadrados."""
    return [each_num ** 2 for each_num in number]




def square_root_list(numbers):
    """
    Esta função calcula a raiz quadrada de cada número da lista.
    :param numbers: Lista de números para os quais a raiz quadrada deve ser calculada.
    :return: Lista de raízes quadradas.
    """
    #escreva seu código aqui
    return [each_num ** 0.5 for each_num in numbers]

# FIXME: Lida com divisão por zero

def divide_list(numbers, divisor):
    """
    Esta função divide cada número da lista pelo divisor.
    :param numbers: Lista de dividendos.
    :param divisor: O divisor.
    :return: Lista de resultados da divisão.
    """
    return [each_num / divisor for each_num in numbers]


class ListCalculator:
    def __init__(self):
        """
        Constructor for the ListCalculator class.
        Initializes without any parameters.
        """
        pass

    def square(self, numbers):
        """
        Squares each number in the list.
        :param numbers: List of numbers to be squared.
        :return: List of squared numbers.
        """
        return [each_num ** 2 for each_num in numbers]

    def square_root(self, numbers):
        """
        Calculates the square root of each number in the list.
        :param numbers: List of numbers for which the square root is to be calculated.
        :return: List of square roots.
        """
        # TODO: Implement the square root method
        return [each_num ** 0.5 for each_num in numbers]

    def divides(self, numbers, divisor):
        """
        Divides each number in the list by the divisor.
        :param numbers: List of dividends.
        :param divisor: The divisor.
        :return: List of results of the division.
        """
        # FIXME: Handle division by zero
        return [each_num / divisor for each_num in numbers]
    
number_list = [1,2,3,4, 25]
calculator = ListCalculator()

print(f"Squared list {calculator.square(number_list)}")
print(f"Squared root list {calculator.square_root(number_list)}")
print(f"Squared divide {calculator.divides(number_list, 2)}")

