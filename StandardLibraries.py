#///////////_1_задача_//////////////

# import numpy as np
# def ListToNumpy(arr):
#     np_arr = np.array(arr, dtype=float)
#     return np_arr
#
# arr_list = [[1, 2, 3], [4, 5, 6]]
# result_array = ListToNumpy(arr_list)
# print(result_array)

#///////////_2_задача_//////////////

# import numpy as np
# def ShapeSizeCalc(arr):
#     shape = arr.shape
#     size = arr.size
#     return shape, size
# arr_array = np.array([[1, 2, 3], [4, 5, 6]])
# shape, size = ShapeSizeCalc(arr_array)
# print(f'Shape: = {shape}, Size: = {size}')

#///////////_3_задача_//////////////

# import numpy as np
# def ArrayIndexing(arr, rows, val):
#     if val < arr.shape[1]:
#         ai_rows = arr[rows]
#         ai_arr = ai_rows[:, :: val]
#         return ai_arr
#     else:
#         return 'Значение VAL не может быть больше или равно длине строки!'
# # тест кода (если ставить val=2 то выхотит [[1 3] [1 3]]
# test = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
# ai_rows = [0, 1]
# val = 3
# n = ArrayIndexing(test, ai_rows, val)
# print(n)

#///////////_4_задача_//////////////

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.arange(1, 10, 0.1)
# y = 6 * x - 2
# plt.plot(x, y)
# plt.title("График функции y = 6x - 2")
# plt.xlabel("Ось  x")
# plt.ylabel('Ось  y')
# plt.show()

#///////////_5_задача_//////////////

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(-10, 10, 0.1)
# y1 = 6 * x**3 - 2 * x + 8
# y2 = 3 * x + 1
#
# plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1)
# plt.plot(x, y1)
# plt.title("График функции F(x, y) = 6x^3 - 2x + 8")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
#
# plt.subplot(1, 2, 2)
# plt.plot(x, y2)
# plt.title("График функции F(x, y) = 3x + 1")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
#
# plt.tight_layout()
# plt.show()

#///////////_6_задача_//////////////

# import matplotlib.pyplot as plt
# vegetables = ['Помидоры', 'Огурцы', 'Тыква', 'Свёкла', 'Редис', 'Картофель']
# counts = [100, 65, 12, 47, 89, 256]
# plt.bar(vegetables, counts)
# plt.ylabel('Колличество')
# plt.title('Товар')
# plt.grid(True)
# plt.show()



