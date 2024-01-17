# TODO Напишите функцию find_common_participants
def find_common_participants(list1, list2, deli=","):
    list1 = list1.split(deli)
    list2 = list2.split(deli)
    list3 = []
    for i in list1:
        for j in list2:
            if i == j:
                list3.append(i)
    list3.sort()
    return list3

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
deli = "|"

print(find_common_participants(participants_first_group, participants_second_group, deli))
