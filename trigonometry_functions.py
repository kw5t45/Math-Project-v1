import math


# sin cos tan log ln
def replace_trigonometry(equation, x):
    # let eq be    x ^ 2 + sinx - sin5
    if "sin" in equation:
        for index, value in enumerate(equation):
            if value == "i":  # since letter "i" is only found in "sin" operation,
                # we are taking sin_parameter based on i's index, therefore
                # i_index + 2
                sin_parameter = equation[index + 2]
                equation = equation.replace("sin" + sin_parameter, str(math.sin(int(sin_parameter))))

    return equation
