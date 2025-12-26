from src.calculator import *


def main() -> None:
    """
    App entry point
    """

    while True:
        expression = input('> ')
        
        if expression == 'exit':
            break
        
        result = evaluate(expression)
        print(result)

if __name__ == "__main__":
    main()
