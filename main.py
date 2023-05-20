#Задана рекуррентная функция. Область определения функции – натуральные числа.
# Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
# Определить границы применимости рекурсивного и итерационного подхода.
# Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
#30. F(1) = 1; F(2) = 2; F(3) = 3, F(n) = F(n-3)*(n-1)/3 при n > 3.
import time
import matplotlib.pyplot as plt
Xst1 = []
Xst2 = []
X = []
def G(w):
    if w == 1:return 1
    if w == 2:return 2
    if w == 3:return 3
    if w> 3:return G(w-3)*G(w-1)/3
def P(n):
    if n == 1:return 1
    if n == 2:return 2
    if n == 3:return 3
    if n >3:
        f = [1] * 5
        f[1] = 2
        f[2] = 3
        for i in range(5, n+1):
            f[4] = f[1]*f[3]/3
            f[0], f[1],f[2],f[3] = f[1],f[2],f[3],f[4]
        return f[4]
print("Введите число для количества вычислений:",end='')
m = int(input())
for i in range(1,m+1):
    print(G(i))
    X.append(i)
print('')
print('№'+' '+'Рекурсивно'+' '+'Итеративно')
for n in range(1,m+1):  # заполнение списков данными
    start = time.perf_counter()
    G(n)
    end = time.perf_counter()
    print(str(n) + ' | ' + str(end - start) + " | ", end='')
    Xst1.append(end - start)
    start = time.perf_counter()
    P(n)
    end = time.perf_counter()
    print(str(end - start))
    Xst2.append(end - start)
y1 = Xst1
y2 = Xst2
plt.xlabel('Число, которое подаётся')
plt.ylabel('Время поиска в миллисекундах')
plt.plot(X, y1, label='Рекурсивно')
plt.plot(X, y2, label='Итеративно')
plt.legend()
print('')
print("Проверка на границы функций")
print("N для двух функций:", end='')
n= int(input())
print('')
if n < 1000:
    print("Значение есть, идёт подсчёт")
    print("Получаем значения для рекурсии:", G(n))
    print("Получаем значения для итерации:", P(n))
elif n >= 1000:
    print("Для рекурсии значения 1000 и выше не считаются и выдаёт ошибку")
    print("Значения для итерации:", paf(n))
plt.show()