# Тема 7. Работа с файлами (ввод, вывод)
### Отчет по Теме #7 выполнил:
- Трофименко Артем Сергеевич
- ПИЭ-21-2

| Задание | Сам. раб. |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №7
## Задание №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.
#### Выполнение:
```python
from collections import Counter
import re

def count_words(text):
    # Используем регулярное выражение для разделения текста на слова
    words = re.findall(r'\b\w+\b', text.lower())

    # Считаем количество использований каждого слова
    word_counts = Counter(words)

    # Находим самое популярное слово и количество его использований
    most_common_word, count = word_counts.most_common(1)[0]

    return most_common_word, count

if __name__ == "__main__":
    # Задайте абсолютный путь к вашему файлу
    file_path = "C:/Users/astro/PycharmProjects/Tema_2/TextFor1.txt"

    try:
        # Читаем текст из файла
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        most_common_word, count = count_words(text)

        # Вывод результатов
        print(f"Самое популярное слово: {most_common_word}")
        print(f"Количество использований: {count}")

    except FileNotFoundError:
        print(f"Файл по пути '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/7f8cace2-f7ee-4068-aba1-965157dd5e8b)

#### Вывод: Программа успешно считывает текст из указанного файла, а затем подсчитывает количество слов и определяет самое популярное слово с его количеством использований. Убедитесь, что указанный путь к файлу верен и файл существует. В случае ошибки при чтении файла программа предоставит соответствующее уведомление.
 
## Задание №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.
#### Выполнение:
```python
import csv
import os
import datetime

def create_expenses_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Дата', 'Сумма', 'Трата'])

def add_expense(file_name, amount, expense):
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file_name, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, amount, expense])

def display_expenses(file_name):
    with open(file_name, 'r', encoding='cp1251', errors='replace') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def main():
    expenses_file = "expenses.csv"

    if not os.path.isfile(expenses_file):
        create_expenses_file(expenses_file)

    while True:
        print("\nВыберите действие:")
        print("1. Добавить расход")
        print("2. Просмотреть расходы")
        print("3. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            amount = input("Введите сумму расхода: ")
            expense = input("Введите трать: ")
            add_expense(expenses_file, amount, expense)
            print("Расход успешно добавлен!")

        elif choice == "2":
            display_expenses(expenses_file)

        elif choice == "3":
            print("Программа завершена.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите существующий вариант.")

if __name__ == "__main__":
    main()
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/f478d377-0a5d-4e0b-b74a-31e630e481f6)
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/da4adfcb-098e-49b7-9690-aff079d38d77)

#### Вывод: Эта программа на Python предоставляет простой механизм учета расходов через консоль. Пользователь может вводить информацию о расходах, которая сохраняется в файле `expenses.json`, и просматривать текущие расходы. Программа обеспечивает удобный способ отслеживания финансов и может быть легко расширена для добавления дополнительных функциональностей по необходимости.

## Задание №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
#### Выполнение:
```python
def get_statistics(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

            # Подсчет количества букв латинского алфавита
            alphabet_letters_count = sum(c.isalpha() and c.isascii() for c in text)

            # Подсчет количества слов
            word_count = len(text.split())

            # Подсчет количества строк
            line_count = text.count('\n') + 1

            return alphabet_letters_count, word_count, line_count
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    file_path = 'input.txt'

    statistics = get_statistics(file_path)

    if statistics is not None:
        alphabet_letters_count, word_count, line_count = statistics
        print(f"Количество букв латинского алфавита: {alphabet_letters_count}")
        print(f"Количество слов: {word_count}")
        print(f"Количество строк: {line_count}")
    else:
        print(f"Файл '{file_path}' не найден.")
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/63ff980d-1409-4c9b-8908-e92d51e0d627)

#### Вывод: Данная программа на Python выполняет анализ текстового файла `input.txt`, выводя статистику, включающую количество букв латинского алфавита, число слов и количество строк. Простота использования и понятность вывода делают этот инструмент удобным для быстрого анализа текстовых данных на латинице. Убедитесь, что файл `input.txt` существует в том же каталоге, что и скрипт, и запустите программу для получения статистики.

## Задание №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
#### Выполнение:
```python
def censor_text(sentence, forbidden_words):
    for word in forbidden_words:
        # Заменяем каждое вхождение слова независимо от регистра
        sentence = sentence.replace(word, '*' * len(word), -1)
    return sentence


def load_forbidden_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            forbidden_words = [word.strip().lower() for word in file.read().split()]
        return forbidden_words
    except FileNotFoundError:
        return None


if __name__ == "__main__":
    sentence = input("Введите предложение: ")

    forbidden_words = load_forbidden_words('input.txt')

    if forbidden_words is not None:
        censored_sentence = censor_text(sentence.lower(), forbidden_words)
        print("Цензурированное предложение:")
        print(censored_sentence)
    else:
        print("Файл 'input.txt' не найден.")
```
#### Результат: 
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/6369fd07-b4f8-48e3-913a-15b7908ab4e7)
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/242c1ee5-2bec-4eb3-a129-8cc6d8307942)

#### Вывод:

## Задание №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
#### Выполнение:
```python
def calculate_average_grade(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            total_students = len(lines)
            total_grades = sum(int(line.split(':')[1].strip()) for line in lines)

            if total_students > 0:
                average_grade = total_grades / total_students
                return average_grade
            else:
                return None
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    file_path = 'students.txt'

    average_grade = calculate_average_grade(file_path)

    if average_grade is not None:
        print(f"Средний балл всех студентов: {average_grade:.2f}")
    else:
        print(f"Файл '{file_path}' не найден или не содержит данных.")
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/3dd14417-19f0-42b8-863c-48840c98ed6b)
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/c84193cb-446a-4e94-83d8-33ef9e67ac70)

#### Вывод: Программа успешно вычисляет средний балл студентов, используя данные из файла `students.txt`, где указаны их имена и оценки. Для этого предоставлены случайные имена и оценки в диапазоне до 5. Пользователь может легко адаптировать эти данные или добавить свои собственные для дополнительного тестирования программы.

## Общий вывод: В ходе решения различных задач на Python, я научился эффективно взаимодействовать с текстовыми файлами, выполнять анализ данных и создавать простые программы для обработки информации. Изучение работы с файлами позволило мне создать программы, способные читать и записывать текстовые данные. Программа для цензурирования текста, анализирующая файл с запрещенными словами, демонстрирует понимание регулярных выражений и методов обработки строк. Решение задачи о среднем балле студентов подчеркивает использование циклов и обработку исключений для обеспечения стабильности программы при работе с файлами. В целом, решение этих задач позволило мне расширить свои навыки программирования на Python и применить их в реальных сценариях.
