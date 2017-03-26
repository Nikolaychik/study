# инициализировать данные для последующего сохранения в файлах
# записи
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}
loliruyu = {'kek': 'KEK', '4ch': 'foch', 'lolets': 'LOL'}
poh = {'NONE': None}

# база данных
db = {}
db['poh'] = poh
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db['loliruyu'] = loliruyu

if __name__ == '__main__':
    # если запускается, как сценарий
    for key in db:
        print(key, '=>\n ', db[key])