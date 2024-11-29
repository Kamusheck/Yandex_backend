#theory 

#1.1
users = ['Степан', 'Анатолий', 'Антон', 'Андрей']
def print_users(users):
    for user in users:
        print(user)
print_users(users)

#1.2
resorts = ['в Сочи', 'на курорты Краснодарского Края', 'в Санкт-Петербург', 'в Карелию']

def choose_vacation_place(resorts):
 # Стёпа, смотри, мы начнём выбор с Карелии, пусть тебе повезёт!
    destination = 'в Карелию'
    for resort in resorts:
        if resort == 'в Сочи':
            destination = resort
            print('Поехали ' + destination)

choose_vacation_place(resorts)

#2.1
# Настройте функцию так, чтобы она не сломалась при вызове без аргументов
def lets_go(name = 'Друг', target='учить Python'):
    print(name + ', пойдём ' + target)

lets_go()

#2.2
def lets_go(name='Друг', target='учить Python'):
    print(name + ', пойдём ' + target)


# Исправьте вызов так, чтобы аргумент был передан
# в параметр с именем target
lets_go(target='читать следующий урок!')

#3.1
# Объявите функцию rooms_equal() с параметрами room_size и room_list
def rooms_equal(room_size,room_list):
    count = 0
    for room in room_list:
        if room == room_size:
            count = count + 1
    print('Комнат площадью', room_size, 'кв.м:', count)
# Перенесите следующий код в тело функции, которую вы объявили





# Следующий код не изменяйте и не переносите в тело функции
flat = [
    5.55, 22.19, 7.78, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]

hut = [9.2, 3.5, 8.1, 2.3, 9.2, 4.2, 6.9]

rooms_equal(5.55, flat)
rooms_equal(9.2, hut)
# Добавьте ещё один вызов функции rooms_equal()
# Передайте в функцию искомую площадь - 9.2 кв.м и список hut

#3.2
def number_of_occurrences(char, string):
    count = 0
    # Она будет хранить количество вхождений
    ...
    for letter in string:
        if char == letter:
            count += 1
        # Напишите условие: сравните переменные letter и char
        # И если letter равна char - увеличивайте счётчик count на 1
        ...

    # Печатаем исходную строку:
    print('Исходная строка:', string)
    # Печатаем результат подсчётов:
    print('Количество вхождений символа', char, 'составляет:', count)
    

# Код ниже не изменяйте
phrase = 'Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили.'

# Вызываем функцию number_of_occurrences(), чтобы она посчитала, 
# сколько раз во фразе phrase встречается буква 'е'
number_of_occurrences('е', phrase)

#3.3
may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25, 17, 19]
may_2018 = [20, 27, 23, 18, 24, 16, 20, 24, 18, 15, 19, 25, 24, 26, 19, 24, 25, 21, 17, 11, 20, 21, 22, 23, 18, 20, 23, 18, 22, 23, 11]

def comfort_count(temperatures):
    count = 0
    for i in temperatures:
        if 22 <= i <= 26:
            count += 1
    print(f'Количество тёплых дней в этом месяце: {count}')
    # Напишите код функции.
    ...
    # Вызовите функцию print()


# Дальше код не меняйте
comfort_count(may_2017)  # Узнаем, что было в мае 2017 г.
comfort_count(may_2018)  # Узнаем, что было в мае 2018 г.

#4.1
may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25, 17, 19]

# Допишите эту функцию
def comfort_count(temperatures):
    count = 0
    for temp in temperatures:
        if 22 <= temp <= 26:
            count += 1
    # Функция должна вернуть значение переменной count
    return count

# Код ниже не изменяйте:
# вызовем функцию comfort_count(), передадим в неё список may_2017,
# результат работы сохраним в переменную nice_days
nice_days = comfort_count(may_2017)

# Напечатаем значение, сохранённое в nice_days
print('Количество тёплых дней в этом месяце:', nice_days)


#4.2
# Функция для вычисления периметра куба.
def calc_cube_perimeter(side):
    return side * 12

# Присвойте переменной one_cube_perimeter значение,
# которое вернёт функция calc_cube_perimeter() с аргументом 3:
# 3 метра - это длина ребра куба.

one_cube_perimeter = calc_cube_perimeter(3)

# Вычислите общую длину палок, необходимых 
# для строительства 8 кубов, 
# и сохраните это значение в переменную full_length 
full_length = 8 * one_cube_perimeter

# А теперь напечатаем результат (в этой строке ничего изменять не нужно)
print('Необходимый метраж палок для 8 кубов:', full_length)

#4.3
# Функция для вычисления площади куба.
def calc_cube_area(side):
    # Формулу для вычисления площади одной грани куба Афанасий написал:
    one_face = side * side

    # Вычислите полную площадь куба: у него шесть одинаковых граней.
    cube_area = one_face * 6 

    # Удалите многоточие и допишите функцию так, 
    # чтобы она возвращала полную площадь куба
    return cube_area


# Присвойте переменной one_cube_area значение,
# которое вернёт функция calc_cube_area() с аргументом 3:
# 3 метра - это длина ребра куба.
one_cube_area = calc_cube_area(3)

# Вычислите общую площадь стекла, необходимого 
# для строительства 8 кубов, 
# и сохраните это значение в переменную full_area 
full_area = 8 * one_cube_area

print('Необходимая площадь стекла для 8 кубов, кв.м:', full_area)


#5.1
# Функция для вычисления периметра кубов.
def calc_cube_perimeter(side):
    return side * 12


# Функция для вычисления площади кубов.
def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6
    return cube_area


# Дополните объявление функции: 
# теперь должна принимать два параметра -
# длину ребра куба и количество кубов.
def calc_cube(side, quantity ):
    # Вызываем функцию, рассчитывающую периметр
    # и передаём в неё размер куба
    one_cube_perimeter = calc_cube_perimeter(side)

    # Здесь вместо многоточия должна стоять переменная, 
    # хранящая количество кубов, переданное во втором аргументе.
    full_length = one_cube_perimeter * quantity

    # Вызываем функцию, рассчитывающую площадь стекла
    # и передаём в неё размер куба
    one_cube_area = calc_cube_area(side)

    # Здесь вместо многоточия должна стоять переменная, 
    # хранящая количество кубов, переданное во втором аргументе.
    full_area = one_cube_area * quantity

    # В этой строке замените многоточие на переменную, хранящую количество кубов
    print('Для', quantity, 'кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', full_area)


# Для проверки работы кода вызываем функцию с двумя аргументами: 
# 3 - это размер ребра куба,
# 2 - это необходимое количество кубов
calc_cube(3, 2)


#5.2
def calc_cube_perimeter(side):
    return side * 12


def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6
    return cube_area


def calc_cube(side, quantity):
    one_cube_perimeter = calc_cube_perimeter(side)
    full_length = one_cube_perimeter * quantity
    one_cube_area = calc_cube_area(side)
    full_area = one_cube_area * quantity
    print('Для', quantity, 'кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', full_area)


calc_cube(2,4)
calc_cube(0.5,26)
calc_cube(0.61,6)

# Каждый вызов должен быть на отдельной строке.