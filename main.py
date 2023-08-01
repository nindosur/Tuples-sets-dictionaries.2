    # 1 кортежи
list1 = [i for i in range(5)]
list2 = [i*i for i in range(5)]
list3 = [i-5*i for i in range(5)]
my_tuple1 = tuple(list1)
print('Первый кортеж', my_tuple1)
my_tuple2 = tuple(list2)
print('Второй кортеж', my_tuple2)
my_tuple3 = tuple(list3)
print('Третий кортеж', my_tuple3)

list4 = []
for i in range(len(my_tuple1)):
    for j in my_tuple2:
        if i == j:
            for l in my_tuple3:
                if l == j:
                    list4.append(l)
print('Элемент, который есть во всех кортежах: ', list4)

# 2
list5 = []
for i in my_tuple1:
    if i not in my_tuple2 and i not in my_tuple3:
        list5.append(i)
for j in my_tuple2:
    if j not in my_tuple1 and j not in my_tuple3:
        list5.append(j)
for l in my_tuple3:
    if l not in my_tuple2 and l not in my_tuple1:
        list5.append(l)
print('Уникальный для каждого списка элемент: ', list5)

# 3
list6 = []
for i in range(len(my_tuple1)):
    if my_tuple1[i] == my_tuple2[i] == my_tuple3[i]:
        list6.append(my_tuple1[i])
print('Элемент, который есть в каждом из кортежей и находится в каждом из кортежей на той же позиции:', list6)