# lesson 6
name = 'Данил'  
surname = 'Марков'
print('Меня зовут ' + name + ' ' + surname + '.')

#lesson 7
temperature = -25
weather = 'солнечно'

print('Сегодня '+ weather)
print('Температура воздуха ' + str(temperature) + ' градусов')


#lesson8.1
speed_kmh = 1079252848.8

speed_kms = speed_kmh / 3600

print('Скорость света равна', int(speed_kms), 'км/с')


#lesson8.2
snake = '38.2'  # Длина Питона в попугаях
length = 6.5  # Количество Питонов, которых можно уложить вдоль вагона.
result = int(float(snake) * length)
print('В вагоне можно положить в ряд',str(result) , 'попугаев')


#lesson9.1
print('Привет, я Анфиса!')
friends = ['Сергей','Соня','Дима','Алина','Егор']
print(friends)

#lesson9.2
friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']
index = 3
print('Привет, ' + friends[index] + ', я Анфиса!')

#lesson9.3
print('Привет, я Анфиса!')
friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']
index = 2

print(friends[index]+ ' живёт в Красноярске')

#lesson9.4
print("Привет, я Анфиса!")
friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']
count = len(friends)
print('У тебя ' + str(count) + ' друзей')