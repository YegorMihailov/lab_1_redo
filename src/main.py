from src.calculator import *


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    while True:
        expression = input('> ')
        
        if expression == 'exit':
            break
        
        result = evaluate(expression)
        print(result)

if __name__ == "__main__":
    main()
