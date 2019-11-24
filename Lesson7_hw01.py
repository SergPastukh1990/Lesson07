#“harry potter; 30; 127.45 galeon; auror”
#“ross geller; 34; 6500.45 usd; paleontologist”
#Необходимо распарсить строку(выбрать одну) и сохранить в словарь информацию о 
# персоне. Для хранения имени, использовать вложенный словарь с ключами first_name, last_name. Для 
# хранения информации о зарплате использовать словарь с ключами - amount и currency.
#На выходе должен быть словарь вида
#{'name': {'first_name': 'Harry', 'last_name': 'Potter'}, 'age': 30,
#'profession': 'auror', 'salary': {'amount': 127.45, 'currency': 'galeon'}}
data = input ('Enter data:')
line1 = data.split("; ")
dictionary = {}
first_name = line1[0].split()
salary = line1[2].split()
dictionary['name'] = {'first_name': first_name[0].capitalize(), 'last_name': first_name[1].capitalize()}
dictionary['age'] = int(line1[1])
dictionary['profession'] = line1[3]
dictionary['salary'] = {'amount': float(salary[0]), 'currency': salary[1]}
print ('line1:', line1)
print ('dict_result:',  dictionary)
#line1 = ("harry potter; 30; 127.45 galeon; auror").split("; ")