# Замер производительности
import random
import datetime


value = 10
fake_list = []

for _ in range(1000000):
    fake_list.append(random.randint(0, 1000))

start = datetime.datetime.now()
found = False
for number in fake_list:
    if number == value:
        found = True
print(found)
print(datetime.datetime.now() - start)

start = datetime.datetime.now()
found = False
i = 0
while i < len(fake_list) and not found:
    if fake_list[i] == value:
        found = True
    i += 1
print(found)
print(datetime.datetime.now() - start)

'''Итого: цикл while отработал в 33 раза быстрее цикла for.
Мы попробовали увеличить длину списка до 10 миллионов - цикл while отработал в 336 раз быстрее.
Это совсем не значит, что цикл while работает быстрее чем for - они работают одинаково эффективно, одинаково быстро. 
Данный пример показывает разницу алгоритмов. Для решения данной конкретной задачи - задачи поиска нужного значения, оптимальнее использовать цикл while. 
Для других задач будет лучшим решением использовать цикл for. Поэтому очень важно перед написанием кода составить алгоритм программы.'''