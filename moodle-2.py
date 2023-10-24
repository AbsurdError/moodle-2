# import random
# # k = random.randrange(1, 60, 6)
# # print(k)
#
# s = ['a', 2, 'b', 4, 5, 'c', 7]
# random.shuffle(s)
# # print(*s)
#
# n = random.choice(s)
# print(n)
# import numpy as np
# a = np.array([1, 2, 3])
#
# print(a)
# import matplotlib.pyplot as plt
# plt.plot([1, 2, 5, 4, 5], [1, 2, 9, 4, 5])
# plt.show()
# import numpy as np
# x = np.linspace(0, 10, 50)
# y1 = x
# y2 = [i**2 for i in x]
#
# plt.figure(figsize=(9, 9))
# plt.subplot(2, 1, 1)
# plt.plot(x, y1)
# plt.title('chatair')
# plt.ylabel('y1', fontsize=14)
# plt.grid(True)
# plt.subplot(2, 1, 2)
# plt.plot(x, y2)
# plt.xlabel('x', fonsize=14)
# plt.show()
#
#
# plt.title('График у=х')
# plt.xlabel('x')
# plt.ylabel('y1, y2')
# plt.grid()
# plt.plot(x, y1, x, y2, 'y-^')
# plt.show()

# import matplotlib.pyplot as plt
# fruits = ['apple', 'orange', 'peatch', 'melon', 'bannana']
# counts = [12, 45, 14, 52, 56]
# plt.bar(fruits, counts)
# plt.show()

# import calendar
# year = int(input('Введите год:  '))
# if calendar.isleap(year):
#     print('Високосный')
# else:
#     print('Не весокосный')


# import calendar
# week = (['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'])
# x = calendar.weekday(1995, 6, 25)
# print(week[x])


# import calendar
# print(calendar.calendar(2023, 2, 2, 6, 3))


# from fuzzywuzzy import fuzz as f
# print(f.ratio('Плохой код на самом деле не плохой.', 'Его просто не так поняли.'))
# print(f.ratio('Работает? Не трогай.', 'Работает? Не трогай.'))
# print(f.ratio('Работает? Не трогай.', 'Работает? Не трогай!'))

