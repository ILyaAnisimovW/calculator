# учебный комит типа фикс калькулятора
def prepare(preparation_example):
    
    preparation_example = preparation_example.split()
    
    if len(preparation_example) != 3:
        return None
    
    one = preparation_example[0]
    action = preparation_example[1]
    two = preparation_example[2]
    
    try:
        one = float(one)
        two = float(two)
        
    except ValueError:
        return None
    
    return one, action, two


def calculate(one, action, two):
    
    actions = {
            '+': lambda one, two: one + two,
            '-': lambda one, two: one - two,
            '*': lambda one, two: one * two,
            '/': lambda one, two: one / two,
            '**': lambda one, two: one ** two,
            '%': lambda one, two: one % two,
            '//': lambda one, two: one // two}

    if action not in actions:
        return None
    
    try:
        return actions[action](one, two)
    
    except ZeroDivisionError:
        return False


def main():
    
    while True:
        
        preparation_example = input("Введите выражение: ")
        if preparation_example == "q": 
            print("Выход>>>")
            break

        example = prepare(preparation_example)
        if example is None:
            print("Ошибка выражения!")
            continue

        result = calculate(*example)
        if result is None:
            print("Ошибка выражения!")
            continue

        if result is False:
            print("Деление на нуль!")
            continue

        print(result)


if __name__ == "__main__":
    main()
