def tokenize(expression: str) -> list:
    """Split a mathematical expression string into tokens
    
    Args:
        expression (str): Mathematical expression as a string
    
    Returns:
        list: List of tokens
    
    Raises:
        ValueError: If expression contains unknown symbols
    """

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

def expr(tokens: list) -> int | float:
    """Parse and evaluate expression level (addition and subtraction)
    
    Handles addition and subtraction operations with left associativity
    
    Args:
        tokens (list): List of tokens
    
    Returns:
        int or float: Result of the expression
    
    Raises:
        ZeroDivisionError: If division by zero occurs
    """

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

def term(tokens: list) -> int | float:
    """Parse and evaluate term level (multiplication and division)
        
    Args:
        tokens (list): List of tokens
    
    Returns:
        int or float: Result of the term
    
    Raises:
        ZeroDivisionError: If division by zero occurs
    """
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


def factor(tokens: list) -> int | float | str:
    """Parse and evaluate factor level (numbers and unary operators)
    
    Args:
        tokens (list): List of tokens
    
    Returns:
        int or float: Parsed number value
        str: 'Invalid expression' if parsing fails
    """

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
  
def evaluate(expression) -> int | float | str:
    """
    Evaluate a mathematical expression string
    
    Args:
        expression (str): Mathematical expression as a string
    
    Returns:
        int or float: Result of the expression
        str: 'Invalid expression' for syntax errors
    
    Raises:
        ZeroDivisionError: If division by zero occurs
        ValueError: If expression contains unknown symbols
    """
    
    try:
        tokens = tokenize(expression)
        return expr(tokens)
    except ZeroDivisionError:
        raise
    except ValueError:
        raise
    except:
        return 'Invalid expression'