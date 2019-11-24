# Создать файл с именем persons.txt и записать в него строки из задания 1 - про Росса и Гарри. 
# Добавьте символ перехода на новую строку \n в конце каждой строки при добавлении в файл.
# f = open  ('/Users/sergiipastukh/Desktop/python_course/Lesson 5/persons1.txt', 'x')
# f.close()
with open('persons1.txt', 'w') as f:
    f.write("harry potter; 30; 127.45 galeon; aurorn\nross geller; 34; 6500.45 usd; paleontologist\n")

with open('persons1.txt') as f:
    print("single line:", f.readlines())


