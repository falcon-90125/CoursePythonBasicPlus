import random #мой код
person = random.choice(['Алиса', 'Боб']) #мой код
print('Персонаж:', person) #мой код

characters = [{'alice_bob': 'Алиса'},
 {'alice_bob': 'Боб',
  'alter_ego': [{'character': 'Ракета'},
                {'character': 'Халк'},
                {'character': 'Дэдпул',
                 'fruits': ['яблоко', 'банан', 'груша', 'груша']},
                {'character': 'Дракс'},
                {'character': 'Капитан америка',
                 'fruits': ['банан', 'груша', 'банан', 'груша']}]},
 {'alice_bob': 'Боб'},
 {'alice_bob': 'Боб',
  'alter_ego': [{'character': 'Звездный лорд'},
                {'character': 'Тор'},
                {'character': 'Железный человек',
                 'fruits': ['яблоко', 'груша', 'груша']},
                {'character': 'Человек паук'},
                {'character': 'Грут',
                 'fruits': ['апельсин', 'апельсин', 'банан']}]},
 {'alice_bob': 'Алиса'},
 {'alice_bob': 'Боб'},
 {'alice_bob': 'Боб',
  'alter_ego': [{'character': 'Человек паук',
                 'fruits': ['банан', 'яблоко', 'яблоко', 'банан']},
                {'character': 'Грут'},
                {'character': 'Халк'},
                {'character': 'Звездный лорд', 'fruits': ['груша', 'апельсин']},
                {'character': 'Ракета',
                 'fruits': ['апельсин', 'яблоко', 'банан']}]},
 {'alice_bob': 'Алиса',
  'alter_ego': [{'character': 'Электра'},
                {'character': 'Джин Грей'},
                {'character': 'Алая ведьма', 'fruits': ['апельсин', 'груша']},
                {'character': 'Китти Прайд',
                 'fruits': ['яблоко', 'груша', 'яблоко']},
                {'character': 'Капитан Марвел'},
                {'character': 'Черная вдова',
                 'fruits': ['яблоко', 'яблоко', 'яблоко']}]},
 {'alice_bob': 'Алиса'}]

person_count = 0  # количество элементов персонажа person
alter_ego_count = 0  # количество элементов персонажа person, которые содержат альтер-эго
alter_ego_with_fruits = 0  # количество альтер-эго, у которых есть фрукты
apple_count = 0  # количество яблок у всех альтер-эго персонажа person

for character in characters:
    if character['alice_bob'] == person:
        person_count += 1
        # Напиши свой код между BEGIN и END
        # BEGIN
for character in characters:
  if character['alice_bob'] == person:
    if 'alter_ego' in character:
      alter_ego_count += 1
      
for character in characters:
  if character['alice_bob'] == person:
    if 'alter_ego' in character:
      for alter_ego in character['alter_ego']:
        if 'fruits' in alter_ego:
          alter_ego_with_fruits += 1
          
for character in characters:
  if character['alice_bob'] == person:
    if 'alter_ego' in character:
      for alter_ego in character['alter_ego']:
        if 'fruits' in alter_ego:
          fruits = alter_ego['fruits']
          for fruit in fruits:
            if fruit == 'яблоко':
              apple_count += 1
        # END

print("Количество записей с персонажем {}: {}".format(person, person_count))
print("Количество записей с персонажем {}, у которых есть альтер-эго: {}".format(person, alter_ego_count))
print("Количество альтер-эго персонажа {}, у которых есть фрукты: {}".format(person, alter_ego_with_fruits))
print("Общее количество яблок у всех альтер-эго персонажа {}: {}".format(person, apple_count))