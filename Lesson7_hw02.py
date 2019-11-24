# написать скрипт для генерации словаря для шифра Цезаря, 
# https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%A6%D0%B5%D0%B7%D0%B0%D1%80%D1%8F
# Выбрать шаг, например 3. Ключи - символы латинского алфавита, в нижнем регистре. 
# Значения - тоже символы, соответствующие ключам согласно шифру.
# То есть скрипт должен формировать словарь вида 
# {‘a’: ‘d’, ‘b’: ‘e’, ‘c’: ‘f’, … , ‘z’: ‘c’ }
alphabet = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())
cipher = ((alphabet[3:]) + (alphabet[0:3]))
cipher_dict = dict(zip(alphabet, cipher))
print (cipher_dict)


