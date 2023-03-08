# Define the supported operators
operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "%": lambda x, y: x % y,
    "<": lambda x, y: x < y,
    ">": lambda x, y: x > y,
    "==": lambda x, y: x == y,
    "!=": lambda x, y: x != y,
    "<=": lambda x, y: x <= y,
    ">=": lambda x, y: x >= y,
    "&&": lambda x, y: x and y,
    "||": lambda x, y: x or y,
}

# Define the state of the simulator
variables = {}

# Define a function to parse and execute statements


def execute(statement):
    # Split the statement into tokens
    tokens = statement.split()

    # If the statement is a variable assignment
    if len(tokens) == 3 and tokens[1] == "=":
        variables[tokens[0]] = evaluate(tokens[2])

    # If the statement is a variable retrieval
    elif len(tokens) == 1:
        print(variables.get(tokens[0], "undefined"))

    # Otherwise, it's an expression
    else:
        print(evaluate(statement))

# Define a function to evaluate expressions


def evaluate(expression):
    # Split the expression into tokens
    tokens = expression.split()

    # If the expression is a single value
    if len(tokens) == 1:
        try:
            return int(tokens[0])
        except ValueError:
            return variables.get(tokens[0], "undefined")

    # If the expression is a binary operation
    elif len(tokens) == 3 and tokens[1] in operators:
        try:
            x = int(tokens[0]) if tokens[0].isdigit(
            ) else variables.get(tokens[0], "undefined")
            y = int(tokens[2]) if tokens[2].isdigit(
            ) else variables.get(tokens[2], "undefined")
            return operators[tokens[1]](x, y)
        except (ValueError, TypeError):
            return "invalid operands"

    # Otherwise, it's an invalid expression
    else:
        return "invalid expression"


# Start the main loop
while True:
    statement = input("> ")
    execute(statement)
