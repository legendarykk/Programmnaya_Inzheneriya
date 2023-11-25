# Тема 11. Декораторы и исключения.
### Отчет по Теме #11 выполнил:
- Трофименко Артем Сергеевич
- ПИЭ-21-2

| Задание | Лаб. раб. | Сам. раб. |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | - |
| Задание 4 | + | - |
| Задание 5 | + | - |

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа 
## Задание №1
Простой итератор, но у него нет гибкой настройки, например его нельзя развернуть. Он работает просто как next(), но нет prev()

#### Выполнение:
```python
numbers = [0, 1, 2, 3, 4, 5]
for item in numbers:
    print(item)
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/5f2044e2-4e13-4dd0-a990-396bff79c514)

## Задание 2
Класс итератор с гибкой настройкой и удобными применением

#### Выполнение:
```python
class CountDown:
    def __init__(self, start):
        self.count = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        return self.count

if __name__ == '__main__':
    counter = CountDown(5)
    for i in counter:
        print(i)
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/49504bbe-793b-4e86-b247-c3f459630903)

## Задание 3
Генератор списка

#### Выполнение:
```python
a = [i ** 2 for i in range(1, 5)]

print('a - ', a)
for i in a:
    print(i)

print ('iter(a) - ', iter(a))
for i in a:
    print(i)
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/9b0fb366-1ed6-4a3c-b43a-0735007af44a)

## Задание 4
Выражения генераторы

#### Выполнение:
```python
b = (i ** 2 for i in range(1, 5))
print(b)
print('first')
for i in b:
    print(i)
print('second')
for i in b:
    print(i)
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/518bc1ee-6f3b-4a0a-b05b-598f09e80d7a)

## Задание 5
Такой же счетчик, как и в первом задании, только это генератор и использует yield

#### Выполнение:
```python
def countdown(count):
    while count >= 0:
        yield count
        count -= 1

if __name__ == '__main__':
    counter = countdown(5)
    for i in counter:
        print(i)
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/ded9fb3c-4708-4c61-a1b2-98c4fc277c94)

## Самостоятельная работа 
## Задание №1
Вас никак не могут оставить числа Фибоначчи, очень уж они вас заинтересовали. Изучив новые возможности Python вы решили реализовать программу, которая считает числа Фибоначчи при помощи итераторов. Расчет начинается с чисел 1 и 1. Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов.
Для реализации этой функции потребуется обратиться к инструкции yield (Она не сохраняет в оперативной памяти огромную последовательность, а дает возможность “доставать” промежуточные результаты по одному). Результатом решения задачи будет листинг кода и вывод в консоль с числом Фибоначчи от 200.

#### Выполнение:
```python
def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fibonacci_sequence = list(fib(10))
print(fibonacci_sequence)

fib_200 = next(fib(200))
print(fib_200)
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/a536a9ae-9a59-4882-9db9-4a39a6ebca1e)

### Вывод:  
Код генерации чисел Фибоначчи: Использует функцию fib, которая создает генератор чисел Фибоначчи, инструкция yield используется для пошагового возврата значений генератора, первые 10 чисел Фибоначчи выводятся в консоль с помощью print(fibonacci_sequence), число Фибоначчи под индексом 200 выводится в консоль с помощью print(fib_200).

## Задание №2
К коду предыдущей задачи добавьте запоминание каждого числа Фибоначчи в файл “fib.txt”, при этом каждое число должно находиться на отдельной строчке. Результатом выполнения задачи будет листинг кода и скриншот получившегося файла.

#### Выполнение:
```python
def fib(n):
    a, b = 1, 1
    with open("fib.txt", "w") as file:
        for _ in range(n):
            file.write(f"{a}\n")
            yield a
            a, b = b, a + b

fibonacci_sequence = list(fib(10))
print(fibonacci_sequence)

fib_200 = next(fib(200))
print(fib_200)
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/57e2c8c3-365d-4c27-bed0-46740be3c119)

### Вывод: Улучшенный код прошлого задания, который записывает числа в txt файл. 

## Общий вывод: Оба кода вместе создают эффективный генератор чисел Фибоначчи и сохраняют их в файл, минимизируя использование ресурсов.
