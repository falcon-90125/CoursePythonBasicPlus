numbers = [101, 202, 505,]

i = 0
while i < len(numbers):
    number = numbers[i]
    if number % 2 == 0:
        print(number)
    i += 1

print('Конец программы')

'''Поиск значения циклом while'''
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]

i = 0
found = False

while i < len(numbers) and not found:
    if numbers[i] == 0:
        print('Нашли на итерации:', i+1)
        found = True
    i += 1

print('Всего итераций выполнено:', i)

'''Переменная found изначально равна False. Как только найдем нужный элемент, мы присвоим переменной found значение True.'''