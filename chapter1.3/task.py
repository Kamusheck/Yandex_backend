#theory
kids = ['Витя', 'Маша', 'Марина']
for kid in kids:
    print ('У Литейного моста')
    print('Я поймал в Неве кита,')
    print('Спрятал за окошко.')
    print('Съела его кошка,')
    print('Помогали два кота…')
    print('Вот и нет теперь кита!')
    print('Ты не веришь другу?')
    print('Выходи из круга!')
    print('* Из круга выходит', kid, '*')
    print()
print('Всё!')

#2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number_1 in numbers:
    for number_2 in numbers:
        print(number_1, '*', number_2, '=', number_1 * number_2)

#3.1
for i in range(1,5):
	print('Я расправлюсь с задачей', i)

print('Я всех победю!')


#3.2
print('Это первый этаж.')
# Первый этаж построен, начинайте строить со второго
for i in range(2,11):
    # Здесь вместо многоточий
    # вставьте номер текущего этажа,
    # вычислите и вставьте номер предыдущего этажа.
    print('А это', i, 'этаж, он на один выше, чем этаж', i-1)


#3.3
months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

for i in reversed(months):
    print(i)

#3.4
countdown_str = ''

for i in reversed(range(0,11)):
    countdown_str = countdown_str + str(i)+', '

countdown_str = countdown_str + 'поехали!'

print(countdown_str)

#4.1
for messages_count in range(6):
    if(messages_count > 0):
        print(f'Новых сообщений: {messages_count}')

#4.2
for messages_count in range(6):
    if messages_count > 0:
        print('Новых сообщений: ' + str(messages_count))
    else:
        print('У вас нет сообщений')

#4.3
for current_hour in range(24):
    if  current_hour <12:
        print('Доброе утро!')

#4.4
for current_hour in range(24):
    if current_hour < 12:
        print('Доброе утро!')
    else:
        print('Добрый день!')
    
#5.1
for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        print('У вас 1 новое сообщение')
    elif messages_count <= 4:
        print('У вас', messages_count, 'новых сообщения')
    else:
        print(f'У вас {messages_count} новых сообщений')
#5.2
for i in range(0, 24):
    print("На часах " + str(i) + ":00.")
    if i <6:
        print('Доброй ночи!')
    elif i < 12:
        print('Доброе утро!')
    elif i <18:
        print('Добрый день!')
    elif i < 23:
        print('Добрый вечер!')
    else:
        print('Доброй ночи!')
#6.1
for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")
    
    if current_hour >= 6 and current_hour <= 11 :  
        print('Доброе утро!')
    elif current_hour >= 12 and current_hour <= 17:  
        print('Добрый день!')
    elif current_hour >= 18 and current_hour <= 22:                       
        print('Добрый вечер!')
    elif current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи!')

#6.2

for i in range(0, 21):
    if i == 0:
        print('У вас нет новых сообщений')
    elif i == 2 or i ==3 or i ==4:
        # напишите ваш код здесь
        print(f'У вас {i} новых сообщения')
    elif i ==1 :
        print('У вас 1 новое сообщение')
    else:
        print(f'У вас {i} новых сообщений')

#7.1
good_boy = True  # Мальчик-то неплохой

if not(good_boy):
    print('Этот в грязь полез')
    print('и рад,')
    print('что грязна рубаха.')
    print('Про такого говорят:')
    print('он плохой, неряха.')
else:
    print('Этот чистит валенки,')
    print('моет сам галоши.')
    print('Он хотя и маленький,')
    print('но вполне хороший.')

#7.2
# Продуктов маловато:
milk = False          # Молока нет.
cereal = True         # Хлопья есть.
eggs = False          # Яиц нет.

# Вставьте логический оператор вместо многоточия.

if milk and cereal or eggs:
    if eggs:
        if milk:
            breakfast = "- омлет"
        else:
            breakfast = "- яичница"
    else:
        breakfast = "- хлопья с молоком"
else:
    if milk:
        breakfast = "- стакан молока"
    elif cereal:
        breakfast = "можно погрызть сухих хлопьев"
    else:
        breakfast = "ничего не будет: разгрузочный день"

print("Сегодня на завтрак", breakfast)

#7.3