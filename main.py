from validation_functions import validate_equation, validate_x

print('''\nMath project v1 takes an equation as input and a given real integer "x" and returns x's value according to 
the given equation. Accepted operators in equation are: "+", "-", "^", "*", "/", "sin","cos", "tan", "costan", "log", 
and "ln". "π" and "e" are also accepted.\n''')

equation = input('''Give equation in "y = ..." form: ''')
x = input('''Give "x": ''')
print('''\n''')


if validate_equation(equation) != True:  # validate_equation function returns True if validation check is passed.
    print(validate_equation(equation))
    quit()
if validate_x(x) != True:
    print(validate_x(x))
    quit()

if "^" in equation:
    equation = equation.replace("^", "**")


input_list = equation.split("=")  # getting equation from input
equation = input_list[1]

x = int(x)
print(eval(equation))