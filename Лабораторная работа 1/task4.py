users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dict={"Общее количество": len(users), "Уникальные посещения":len(set(users))}
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
print(dict)