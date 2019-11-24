# Открыть файл из п.3 в режиме чтения, прочитать из него содержимое, 
# распарсить ее в словарь вида persons = {‘ross’: {информация про Роса в виде словаря}, ‘harry’: {информация про Гарри в виде словаря}}.
with open('/Users/sergiipastukh/Desktop/python_course/Lesson 5/persons1.txt') as f:
   info = (f.readlines())
# dictionary = {'ross': info}
harry_info = info[0].split("; ")
ross_info = info[1].split("; ")

harry_dictionary = {}
h_first_name = harry_info[0].split()
h_salary = harry_info[2].split()
harry_dictionary['name'] = {'first_name': h_first_name[0].capitalize(), 'last_name': h_first_name[1].capitalize()}
harry_dictionary['age'] = int(harry_info[1])
harry_dictionary['profession'] = str((harry_info[3].split("\n"))[0])
harry_dictionary['salary'] = {'amount': float(h_salary[0]), 'currency': h_salary[1]}

ross_dictionary = {}
r_first_name = ross_info[0].split()
r_salary = ross_info[2].split()
ross_dictionary['name'] = {'first_name': r_first_name[0].capitalize(), 'last_name': r_first_name[1].capitalize()}
ross_dictionary['age'] = int(ross_info[1])
ross_dictionary['profession'] = str((ross_info[3].split("\n"))[0])
ross_dictionary['salary'] = {'amount': float(r_salary[0]), 'currency': r_salary[1]}

general_dict = {'ross': ross_dictionary, 'harry': harry_dictionary}
print ('dict_result:',  general_dict)