def tokenize(expression: str):
    tokens = []
    current_number = ''

    expression = expression.replace(' ', '')

    for char in expression:
        if char.isdigit() or char == '.':
            current_number += char
        elif char in "+-*/":
            if current_number:
                tokens.append(current_number)
                current_number = ''
            tokens.append(char)
        else:
            raise ValueError('Unknown symbol')
    
    if current_number:
        tokens.append(current_number)

    return tokens

def expr(tokens):
    try:
        res = term(tokens)

        while tokens and (tokens[0] == '+' or tokens[0] == '-'):
            operator = tokens.pop(0)
            number_2 = term(tokens)

            if operator == '+':
                res += number_2
            else:
                res -= number_2
        
        return res
    except ZeroDivisionError:
        raise

def term(tokens):
    res = factor(tokens)

    while tokens and (tokens[0] == '*' or tokens[0] == '/'):
        operator = tokens.pop(0)
        number_2 = factor(tokens)

        if operator == '*':
            res *= number_2
        elif operator == '/' and number_2 == 0:
            raise ZeroDivisionError
        else:
            res /= number_2
    
    return res           


def factor(tokens: list):
    try:
        token = tokens.pop(0)

        if token in '+-':
            number = tokens.pop(0)

            if '.' in number:
                number = float(number)
            else:
                number = int(number)
            
            if token == '-':
                return -1 * number
            return number

        if '.' in token:
            return float(token)
        
        return int(token)

    except:
        return 'Invalid expression'
  
def evaluate(expression):
    try:
        tokens = tokenize(expression)
        return expr(tokens)
    except ZeroDivisionError:
        raise
    except ValueError:
        raise
    except:
        return 'Invalid expression'