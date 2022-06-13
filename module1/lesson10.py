str1 = 'Сегодня'
str2 = '26 июля'
str3 = 'хороший день'

result = str1 + ' ' + str2 + ' ' + str3 +' для игр'
print(result)

result_f = '{} {} {} для игр'.format('Сегодня', '26 июля', 'хороший день')
print(result_f)

result_f2 = '{} {} {} для игр'.format(str1, str2, str3)
print(result_f2)

result_f3 = '{1} {2} {0} для игр'.format(str1, str2, str3)
print(result_f3)

result_f4 = f'{str1} "{str2}" {str3} для игр'
print(result_f4)

str4 = 'Никаких больше игр'
result_f5 = '''
Сегодня 26 июля - хороший день.
Никаких больше игр!
'''
print(result_f5)

result_f6 = f'''
{str1} {str2} - {str3} для игр!
{str4}.
'''
print(result_f6)

result_f7 = f'{str1} {str2} - {str3} для игр.\n{str4}!'
print(result_f7)

str4 = 'Никаких больше'
str5 = 'вечеринок'
result_f8 = f'{str1} {str2} - {str3} для {str5}.\n{str4} {str5}!'
print(result_f8)

my_string = 'а,б,В,Г,д,Д,д'
print(my_string.upper())
print(my_string.lower())
print(my_string.lower().count('д'))
print(my_string.capitalize()) #делает 1й символ заглавным, все остальные в нижний регистр

my_string_lower = my_string.lower()
my_string_len = len(my_string_lower)
print(f'Длина строки my_string_lower = {my_string_len}')

