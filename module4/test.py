friends = [{'cities': [{'population': 15, 'title': 'к. Усть-Ордынский'},
             {'population': 298765, 'title': 'п. Кировск (Мурм.)'},
             {'population': 200453, 'title': 'д. Клин'},
             {'population': 114243, 'title': 'клх Макаров'},
             {'population': 97232, 'title': 'ст. Муром'},
             {'population': 11, 'title': 'п. Бомнак'}],
  'gender': 'male',
  'job': 'Таможенник',
  'name': 'Влас'}]

# friends_names = []
# friends_jobs = []

# #print(friends['name'])
# friends_names.append(friends[0]['name'])
# friends_jobs.append(friends[0]['job'])

# print(friends_names)
# print(friends_jobs)

friends_cities = []
for title in friends[0]['cities']:
    friends_cities.append(title['title'])

population_list= []
for population in friends[0]['cities']:
  population_list.append(population['population'])

big_city = friends_cities[population_list.index(max(population_list))]

print("Город с самым большим населением:", big_city)