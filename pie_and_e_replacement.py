import math

def replace_pie_and_e(equation):
    if "π" in equation:
        equation = equation.replace("π", str(math.pi))
    if "e" in equation:
        equation = equation.replace("e", str(math.e))
    return equation