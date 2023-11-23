### Отчет по Теме #8 выполнил:
- Трофименко Артем Сергеевич
- ПИЭ-21-2

| Задание | Лаб. раб. | Сам. раб. |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
## Задание №1
### Создайте класс “Car” с атрибутами производитель и модель. Создайте
объект этого класса. Напишите комментарии для кода, объясняющие
его работу. Результатом выполнения задания будет листинг кода с
комментариями.
#### Выполнение:
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

myCar = Car("Toyota", "Mazda")
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/c497e6fb-fb6b-46b9-85d1-1a447005d728)

## Задание №2
### Дополните код из первого задания, добавив в него атрибуты и методы
класса, заставьте машину “поехать”. Напишите комментарии для кода,
объясняющие его работу. Результатом выполнения задания будет
листинг кода с комментариями и получившийся вывод в консоль
#### Выполнение:
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def drive(self):
        print(f"Driving the {self.make} {self.model}")

myCar = Car("Toyota", "Mazda")
myCar.drive()
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/a07c1bef-18fa-4abc-bf21-dd412b84b4c8)

## Задание №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом
емкость батареи. Реализуйте его наследование от класса, созданного в
первом задании. Заставьте машину поехать, а потом заряжаться. Напишите комментарии для кода, объясняющие его работу.
Результатом выполнения задания будет листинг кода с комментариями
и получившийся вывод в консоль.

#### Выполнение
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):

        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 75)

my_electric_car.drive()

my_electric_car.charge()
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/54d063a0-1d54-47f5-9a7a-a0852089b9f1)

## Задание №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании.
Создайте защищенный атрибут производителя и приватный атрибут
модели. Вызовите защищенный атрибут и заставьте машину поехать.
Напишите комментарии для кода, объясняющие его работу.
Результатом выполнения задания будет листинг кода с комментариями
и получившийся вывод в консоль.
#### Выполнение:
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

myCar = Car("Toyota", "Corolla")
print(myCar.make)
myCar.drive()
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/be67a5b9-b8ff-4a64-98f9-e2684593b29c)

## Задание №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а
также еще два класса “Rectangle” и “Circle”. Внутри последних двух
классов реализуйте методы для подсчета площади фигуры. После этого
создайте массив с фигурами, поместите туда круг и прямоугольник,
затем при помощи цикла выведите их площади. Напишите
комментарии для кода, объясняющие его работу. Результатом
выполнения задания будет листинг кода с комментариями и
получившийся вывод в консоль
#### Выполнение:
```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

myRectangle = Rectangle(20, 30)

result1 = myRectangle.area()

myCircle = Circle(20)
result2 = myCircle.area()

print(result1)
print(result2)
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/7b084a6f-669f-4dbd-b5a6-b140950e1c6b)

## Самостоятельная работа №1
## Задание №1
### Самостоятельно создайте класс и его объект. Они должны
отличаться, от тех, что указаны в теоретическом материале
(методичке) и лабораторных заданиях. Результатом выполнения
задания будет листинг кода и получившийся вывод консоли.
#### Выполнение:
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/831b1df0-9461-42f6-b197-bbb2c2445a78)

#### Вывод: класс, представляющий книгу, и объект этого класса.

## Задание №2
### Самостоятельно создайте атрибуты и методы для ранее созданного
класса. Они должны отличаться, от тех, что указаны в
теоретическом материале (методичке) и лабораторных заданиях.
Результатом выполнения задания будет листинг кода и
получившийся вывод консоли.
#### Выполнение:
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")

my_book = Book("Anna Carenina", "Tolstoi")

my_book.info()
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/698ee554-259a-4ab1-9050-7aee742e1bac)

### Вывод:класс, представляющий книгу, и объект этого класса. В этом примере книга будет иметь атрибуты title (название) и author (автор), а также метод display_info(), который выводит информацию о книге.

## Задание №3
### Самостоятельно реализуйте наследование, продолжая работать с
ранее созданным классом. Оно должно отличаться, от того, что
указано в теоретическом материале (методичке) и лабораторных
заданиях. Результатом выполнения задания будет листинг кода и
получившийся вывод консоли

#### Выполнение:
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")

my_book = Book("Anna Carenina", "Tolstoi")



class EBook(Book):
    def __init__(self, title, author, format):
        super().__init__(title, author)
        self.format = format

    def info(self):
        super().info()
        print(f"Format: {self.format}")

my_ebook = EBook("Anna Carenina", "Tolstoi", "PDF")

my_ebook.info()
```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/34b41a0f-b206-45d3-9abb-ada9d3d00ae2)

### Вывод: Использовано наследование для создания нового класса EBook, который расширяет функциональность базового класса Book и добавляет новый атрибут format. Метод info в EBook был переопределен для учета нового атрибута и одновременно использования функциональности родительского класса.

## Задание №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с
ранее созданным классом. Она должна отличаться, от того, что
указана в теоретическом материале (методичке) и лабораторных
заданиях. Результатом выполнения задания будет листинг кода и
получившийся вывод консоли.

#### Выполнение:
```python
class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def info(self):
        print(f"Book Title: {self._title}")
        print(f"Author: {self._author}")

class EBook(Book):
    def __init__(self, title, author, format):
        super().__init__(title, author)
        self._format = format

    def get_format(self):
        return self._format

    def set_format(self, format):
        self._format = format

    def info(self):
        super().info()
        print(f"Format: {self.get_format()}")

my_ebook = EBook("Anna Carenina", "Tolstoi", "PDF")

my_ebook.set_title("New Title")

my_ebook.info()

```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/fbc0fd5b-6804-4c72-9fdf-82a52bd4b504)

#### Вывод: Атрибуты title, author и format закрытыми (приватными) и предоставим методы для получения и установки этих значений. Таким образом, мы скрываем прямой доступ к атрибутам и обеспечиваем контролируемый доступ к данным.

## Задание №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться,
от того, что указан в теоретическом материале (методичке) и
лабораторных заданиях. Результатом выполнения задания будет
листинг кода и получившийся вывод консоли.

#### Выполнение:
```python
class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def info(self):
        print(f"Book Title: {self._title}")
        print(f"Author: {self._author}")

    def read(self):
        print("Reading a physical book.")

class EBook(Book):
    def __init__(self, title, author, format):
        super().__init__(title, author)
        self._format = format

    def get_format(self):
        return self._format

    def set_format(self, format):
        self._format = format

    def info(self):
        super().info()
        print(f"Format: {self.get_format()}")

    def read(self):
        print("Reading an ebook.")

my_book = Book("Anna Carenina", "Tolstoi")
my_ebook = EBook("Padenie", "Kamu", "PDF")

my_book.read()
my_ebook.read()

```
#### Результат:
![image](https://github.com/legendarykk/Programmnaya_Inzheneriya/assets/146570109/8f63c598-b9eb-48ce-966d-9435f7e03402)

#### Вывод: Использованн полиморфизм, где метод read представляет общий интерфейс для чтения книг, но каждый подкласс (Book и EBook) предоставляет свою уникальную реализацию этого метода.

## Общий вывод: 
Объектно-ориентированное программирование (ООП) в Python, как и в других языках программирования, предоставляет ряд преимуществ и инструментов для более удобной и эффективной разработки программ. 
