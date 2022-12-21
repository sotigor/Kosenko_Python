
main_menu = """
            Введите порядковый номер тестового задания (1,2,3 или 4), которое хотите проверить:
            1. Составить алгоритм: если введенное число больше 7, то вывести "Привет".
            2. Составить алгоритм: если введенное имя совпадает с Вячеслав, то вывести “Привет, Вячеслав”,
               если нет, то вывести "Нет такого имени".
            3. Составить алгоритм: на входе есть числовой массив, необходимо вывести элементы массива кратные 3.
            4. Дана скобочная последовательность: [((())()(())]]
               - Можно ли считать эту последовательность правильной?
               - Если ответ на предыдущий вопрос “нет” - то что необходимо в ней изменить, чтоб она стала правильной?

            Для выхода введите: "q" 
            """
assign_menu_3 = """
            Задание 3. Выберите один из следующих вариантов проверки алгоритма: 
                
                - задать свой числовой массив - введите '1';
                
                - использовать предзаданный массив: [0, -3, 3, 2, 6, 8, 24, 6.1] - введите '2';
                
                - вернуться в предыдущее меню - введите 'q'.                        
                """
assign_menu_4 = """
            Задание 4. Выберите один из следующих вариантов:
                
                - вывести на экран ответ по заданию 4 в текстовой форме - введите 1;
                
                - проверить алгоритм с предзаданной (указанной в тестовом задании) скобочной 
                  последовательностью [((())()(())]] - введите 2;
                 
                - проверить алгоритм с скобочной последовательностью, заданной пользователем - введите 3;
                
                - вернуться в предыдущее меню - введите 'q'.
             """
assign_answer_4 = """ 
Задание 4. Ответ в текстовой форме:   
1. [((())()(())]] данную скобочную последовательность нельзя считать правильной.
2. Чтобы данная скобочная последовательность стала правильной необходимо:
   2.1 чтобы количество открытых круглых "(" и квадратных "[" скобок было равным соответствующим закрытым круглым ")" 
   и квадратным "]" скобкам;
   2.2 чтобы сооблюдалась последовательность: сначала идет открытая скобка, а затем закрытая.
   2.3 чтобы сооблюдалась последовательная вложенность пар скобок.

   Таким образом данная скобочная последовательность [((())()(())]] станет правильной, если в неё 
   с учетом п.п.2.2 и 2.3 добавить:
   - одну открытую квадратную скобку "[";
   - одну закрытую круглую скобку ")".

Для возврата в предыдущее меню введите 'q'.
"""

# Функция для задания 1: обработка числового значения
def number_handler(user_number):
    # Обработка целого или дробного положительного или отрицательного числа
    if is_number_int_float(user_number) and float(user_number) > 7:
            print('Привет')
    elif is_number_int_float(user_number) and float(user_number) <= 7:
            print()
    # Обработка не числового значения
    else:
        print("Введеное значение не является числом.")

# Функция для задания 1: проверка является ли вводимое значение числом
def is_number_int_float(str_mean: str):
    try:
        float(str_mean)
        return True
    except ValueError:
        return False

# Функция для задания 2: обработка введенного имени.
def name_handler(user_name):
    if user_name == 'Вячеслав':
        print(f'Привет, {user_name}')
    else:
        print('Нет такого имени.')

# Предзаданный набор чисел для проверки кратности 3
list_numbers = [0, -3, 3, 2, 6, 8, 24, 6.1]

# Функция для задания 3: проверка чисел на соответствие условию (кратность 3).
def check_list(numbers=list_numbers):
    print(f"Числа в массиве {numbers} кратные 3: ")
    sorted_numbers = [print(i) for i in numbers if i % 3 == 0 and i != 0]
    if len(sorted_numbers) == 0:
        print("отсутствуют")

# Функция для задания 3: Перевод из строки в лист с целыми числами
def modify_to_list(numbers_in_string: str) -> list:
    return [int(i) for i in numbers_in_string.split(",") if is_number_int(i)]

# Функция для задания 3: Проверка возможности конвертировать введенное значение в число
def is_number_int(str_mean: str):
    try:
        int(str_mean)
        return True
    except ValueError:
        return False

# Скобочная последовательность заданная в тестовом задании 4
defined_brackets_seq = '[((())()(())]]'

# Инициализация переменнных для задания 4
square_brackets = []
round_brackets = []
br_dict = {'(': ')', ')': '(', '[': ']', ']': '['}

# Функция для задания 4: Проверка правильности скобочной последовательности
def check_brackets_seq(user_brackets_seq: str = defined_brackets_seq):
    """
    Print the message about rightness of given brackets sequence.

    :param user_brackets_seq: Brackets sequence string
    :return: None
    """

    #Обнуление переменных, чтобы не накапливались результаты с предыдущих итераций
    square_brackets = []
    round_brackets = []

    #Формируем скобочные последовательности для используемых скобок
    for i in user_brackets_seq:
        if i in ['(', ')']:
            round_brackets.append(i)
        if i in ['[', ']']:
            square_brackets.append(i)
    brackets_str_square = ''.join(square_brackets)
    brackets_str_round = ''.join(round_brackets)
    # Обнуление переменных, чтобы не накапливались результаты с предыдущих итераций
    r_br_unpaired = []
    sq_br_unpaired = []

    r_br_unpaired = list(check_unpaired_brackets(brackets_str_round, '()'))
    sq_br_unpaired = list(check_unpaired_brackets(brackets_str_square, '[]'))

    # Обнуление переменных, чтобы не накапливались результаты с предыдущих итераций
    r_br_unpaired_unique = []
    sq_br_unpaired_unique = []
    r_br_unpaired_unique = list(set(r_br_unpaired))
    sq_br_unpaired_unique = list(set(sq_br_unpaired))

    # Проверка неправильной вложенности скобок, если скобки в парном количестве
    # (когда используется несколько видов скобок)
    incor_nested_br = check_nested_brackets(user_brackets_seq)

    # Проверка есть ли скобки в заданной скобочной последовательности
    is_brackets_in_seq = []
    is_brackets_in_seq = [i for i in br_dict if i in user_brackets_seq]

    # Печать на экран
    if len(is_brackets_in_seq) == 0:
        print(f'Введенное выражение не содержит круглых или квадратных скобок!')
    else:
        if len(r_br_unpaired) == 0 and len(sq_br_unpaired) == 0 and len(incor_nested_br) == 0:
            print(f'Cкобочная последовательность {user_brackets_seq} является правильной!')
        elif len(r_br_unpaired) == 0 and len(sq_br_unpaired) == 0 and len(incor_nested_br) != 0:
            print(f"Cкобочная последовательность {user_brackets_seq} является неправильной, поскольку не сооблюдается \n"
                  f"последовательная вложенность пар скобок и она содержит следующие неправильные последовательности скобок:\n"
                  f"{incor_nested_br}")
        else:
            print(f'Cкобочная последовательность {user_brackets_seq} является неправильной! \n'
                  f'Для того, чтобы сделать её правильной нужно добавить:')
            if len(r_br_unpaired) != 0:
                print(f"- '{br_dict[r_br_unpaired_unique[0]]}' кругл{'ую' if len(r_br_unpaired) == 1 else 'ые'}"
                      f" скобк{'у' if len(r_br_unpaired) == 1 else 'и'}"
                      f" {r_br_unpaired.count(r_br_unpaired_unique[0])} шт.{';' if len(r_br_unpaired_unique) == 2 else ''}")
                if len(r_br_unpaired_unique) == 2:
                    print(f"- '{br_dict[r_br_unpaired_unique[1]]}' кругл{'ую' if len(r_br_unpaired) == 1 else 'ые'}"
                          f" скобк{'у' if len(r_br_unpaired) == 1 else 'и'}"
                          f" {r_br_unpaired.count(r_br_unpaired_unique[1])} шт.{';' if len(sq_br_unpaired) != 0 else ''}")

            if len(sq_br_unpaired) != 0:
                print(f"- '{br_dict[sq_br_unpaired_unique[0]]}' квадратн{'ую' if len(sq_br_unpaired) == 1 else 'ые'} "
                      f"скобк{'у' if len(sq_br_unpaired) == 1 else 'и'}"
                      f" {sq_br_unpaired.count(sq_br_unpaired_unique[0])} шт. {';' if len(sq_br_unpaired_unique) == 2 else ''}")
                if len(sq_br_unpaired_unique) == 2:
                    print(
                        f"- '{br_dict[sq_br_unpaired_unique[1]]}' квадратн{'ую' if len(sq_br_unpaired) == 1 else 'ые'} "
                        f"скобк{'у' if len(sq_br_unpaired) == 1 else 'и'}"
                        f" {sq_br_unpaired.count(sq_br_unpaired_unique[1])} шт.")


# Функция для задания 4: Определение скобок не имеющих пары
def check_unpaired_brackets(brackets_seq: str, brackets_type: str) -> str:
    """
    Finding brackets that don't have their pair.
    :param brackets_seq: sequence
    :param brackets_type: the pair of analyzing brackets (for instance: "()")
    :return: brackets without their pair or empty string
    """
    if brackets_type not in brackets_seq:
        return brackets_seq
    else:
        return check_unpaired_brackets(''.join(brackets_seq.split(brackets_type)), brackets_type)

# Функция для задания 4: Проверка, что скобки вложены правильно
# (выполняется после проверки парности скобок, имеет смысл, когда разные виды скобок используются)
def check_nested_brackets(brackets_seq: str) -> str:
    """
    Finding incorrectly nested brackets .
    :param brackets_seq: sequence
    :return: string with incorrectly nested brackets
    """
    if '()' not in brackets_seq and '[]' not in brackets_seq:
        return brackets_seq
    else:
        arg = ''.join((''.join(brackets_seq.split('()'))).split('[]'))
        return check_nested_brackets(arg)

# Программа для проверки тестовых заданий
while True:
    # Главное меню
    user_choice = input(main_menu)
    # Запуск проверки задания 1
    if user_choice == "1":
        while True:
            user_number = input("Задание 1. Введите число ('q' - назад): ")
            # Возврат в главное меню
            if user_number == "q":
                break
            number_handler(user_number)
    # Запуск проверки задания 2
    elif user_choice == "2":
        while True:
            user_name = input("Задание 2. Введите имя ('q' - назад): ")
            if user_name == "q":
                break
            name_handler(user_name)
    # Запуск проверки задания 3
    elif user_choice == "3":
        while True:
            # Меню задания 3
            assign_choice_3 = input(assign_menu_3)
            # Пользователь сам задает числовой массив
            if assign_choice_3 == "1":
                while True:
                    user_list = input("Введите целые числа через запятую ('q' - назад): ")
                    # Возврат в меню задания 3
                    if user_list == "q":
                        break
                    # Обработка числового массива пользователя
                    mod_user_list = modify_to_list(user_list)
                    check_list(numbers=mod_user_list)

            # Работа с предзаданным числовым массивом
            elif assign_choice_3 == "2":
                while True:
                    check_list()
                    res_exec_assign_3 = input("Для возврата в предыдущее меню введите 'q':  ")
                    # Возврат в меню задания 3
                    if res_exec_assign_3 == "q":
                        break
            # Возврат в главное меню
            elif assign_choice_3 == "q":
                break
    # Запуск проверки задания 4
    elif user_choice == "4":
        while True:
            # Меню задания 4
            assign_choice_4 = input(assign_menu_4)
            # Вывод ответа в текстовой форме
            if assign_choice_4 == "1":
                while True:
                    # Возврат в меню задания 4
                    answer_text = input(assign_answer_4)
                    if answer_text == "q":
                        break
            # Работа с предзаданной скобочной последовательностью
            if assign_choice_4 == "2":
                while True:
                    check_brackets_seq()
                    res_exec_assign_4 = input("Для возврата в предыдущее меню введите 'q':  ")
                    # Возврат в меню задания 4
                    if res_exec_assign_4 == "q":
                        break
            # Работа с заданной пользователем скобочной последовательностью
            if assign_choice_4 == "3":
                while True:
                    user_brackets_set = input("Введите скобочную последовательность, используя "
                                              "квадратные и (или) круглые скобки ('q' - назад):  ")
                    # Возврат в меню задания 4
                    if user_brackets_set == "q":
                        break

                    # Обработка скобочной последовательности пользователя
                    check_brackets_seq(user_brackets_seq=user_brackets_set)

            # Возврат в главное меню
            if assign_choice_4 == "q":
                break
    # Возврат в главное меню
    elif user_choice.lower() == "q":
        exit()
