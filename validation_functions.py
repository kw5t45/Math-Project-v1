def validate_equation(equation):
    # input validation:

    eq = equation

    if eq.count("=") > 1:
        return ('''"=" Must be only once in input!\n\n\n''')


    # -------------- validation of y--------------------

    y_and_equation_list = eq.split("=")

    # ["y", "<equation>"]

    should_be_y = y_and_equation_list[0].strip()

    if should_be_y != "y":
        return '''Equation must be given in "y = ..." form only!\n'''


    # -----------------------validation of equation--------------------------

    should_be_equation = y_and_equation_list[1].strip()

    # removing trig. operators to validate

    should_be_equation = should_be_equation.replace("sin", "")
    should_be_equation = should_be_equation.replace("cos", "")
    should_be_equation = should_be_equation.replace("tan", "")
    should_be_equation = should_be_equation.replace("costan", "")
    should_be_equation = should_be_equation.replace("log", "")
    should_be_equation = should_be_equation.replace("ln", "")

    trigonometry_operators = ["sin", "cos", "tan", "costan", "log", "ln"]

    wanted_characters = ["(", ")", "x", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "^", "*", "/"]

    for char in should_be_equation:
        if char not in wanted_characters:
            return ('''Supported operators are: "+", "-", "^", "*", "/" "sin","cos", "tan", "costan", "log", 
            and "ln."\n''')
            quit()

    return True


def validate_x(x):
    nums = "1234567890"
    num = x.strip()
    for i in num:
        if i not in nums:
            return '''X must be a real integer!'''
    return True
