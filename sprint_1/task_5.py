# Convert a certain expression like 2+3 to expression in a postfix notation.
# The given expression can have one of the following tokens:
  # a number;
  # a parenthesis;
  # arithmetic operator:
  # subtraction (-);
  # addition (+);
  # multiplication (*);
  # devision (/);
  # modulo operation (%).
# Example:
  # For expression = ["2","+","3"] the output should be ["2","3","+"].
  # [execution time limit] 4 seconds (py)
  # [input] array.string expression
  # An array of tokes of a valid expression in the standard notation.
  # [output] array.string
    # Tokens of the expression in the postfix notation.
# Answer:(penalty regime: 0 %)

def toPostFixExpression(e):
    def precedence(operator):
        if operator in {'+', '-'}:
            return 1
        elif operator in {'*', '/', '%'}:
            return 2
        return 0
    output = []
    operators = []
    for token in e:
        if token.isnumeric():
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Discard '('
        elif token in {'+', '-', '*', '/', '%'}:
            while operators and precedence(operators[-1]) >= precedence(token):
                output.append(operators.pop())
            operators.append(token)
    while operators:
        output.append(operators.pop())
    return output
