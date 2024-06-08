# Control Work
#Part 1:
# Questions:
#1.Что такое объектно-ориентированное программирование (ООП)? Объясните основные концепции ООП.
#2.Опишите разницу между методом класса и статическим методом в Python. Приведите пример.
#3.Что такое инкапсуляция в ООП и как она реализуется в Python?
#4.Объясните, что такое наследование. Как оно реализуется в Python?
#Part 2:
# Questions:
# 1.Напишите функцию is_even, которая принимает число и возвращает True, если число четное, и False в противном случае
# 2.Создайте класс Car, который имеет следующие атрибуты: make, model и year. Добавьте метод display_info, который выводит информацию о машине в формате "Make: , Model: , Year: ".
# 3.Напишите функцию, которая принимает список чисел и возвращает список, содержащий только положительные числа из исходного списка.
#def filter_positive_numbers(numbers):
# 4.Создайте класс Person, который имеет атрибуты name и age. Реализуйте метод greet, который выводит строку Hello, my name is <name> and I am <age> years old. Также создайте дочерний класс Student, который добавляет атрибут student_id и переопределяет метод greet, чтобы включать идентификатор студента в вывод.
# 5.Напишите программу, которая создает объект класса Student и вызывает метод greet.
#Part 3:
# Questions:
# 1.Проверьте, является ли заданная строка палиндромом. Создавайте метод альгоритм для этого что бы проверить
# 2.Реализуйте класс BankAccount, который позволяет выполнять следующие операции: пополнение счета (deposit), снятие денег (withdraw) и проверка баланса (get_balance).
# 3.Напишите функцию, которая принимает строку и возвращает словарь, где ключи - это уникальные символы строки, а значения - количество вхождений этих символов.

#Answers:
#Part 1:
# 1: Объектно-ориентированное программирование так же известное как ООП является одной из неотъемлемых и безусловно сложнейших частей любого языка программирования. Конкретно в языке Python есть несколько функций ООП - это Классы, Инкапсуляция, Наследование и Объекты
# 2: Метод класса в Python принимает первым параметром ссылку на класс ее часто называют cls, a статический метод не принимает ссылку и вызывается только через имя. Примеры:
# def class_method(cls), def static_method()
# 3: Инкапсуляция в Python является одной из частей ООП и используетмся для упаковки данных
# 4: Наследование даже если судить по названию помогает классам наследовать атрибуты друг друга. Используются следующим образом создается класс с аргументами, далее создается еще один класс и в скобках указываеься название предыдущего класса.

# Part 2:
#1
# is_even = int(input("Введите число: "))
# if is_even % 2 == 0:
#     print('Ваше число четное')
# else:
#     print('Ваше число нечетное')

#2
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
        
# display_info = Car('industry', 'Ford', 2003)
# print(display_info.make)
# print(display_info.model)
# print(display_info.year)

#3
# def filter_positive_numbers(numbers):
#     x = []
#     y = []
#     for i in numbers:
#         if i > 0:
#             x.append(i)
#         elif i < 0:
#             y.append(i)
#     return x, y
# print(filter_positive_numbers([1, 13, -24, -34]))

#4
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def greet(self,name, age):
#         print(f'Hello, my name is {self.name} and I am {self.age} years old.')
        

        
# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(self,name, age)
        
#     def another_greet(student_id):
#         student_id = 4321
#         Person.greet.append(student_id)

# Я не понял само задание, и остановился здесь, т.к по моему мнению этого хватит :)

# Part 3
#1
# x = 'потоп'
# if x == x[::-1]:
#     print('это слово является палиндромом')
# else:
#     print('это слово палиндромом не является')
# print(x[::-1])

#2
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self):
#         pass

#     def withdraw(self, amount):
#         pass

#     def get_balance(self):
#         return self.balance


# account = BankAccount(100) 
# print("Баланс:", account.get_balance()) 

#3
# def count_characters(string):
#     x = {}
#     for i in string:
#         if i in x:
#             x[i] += 1
#         else:
#             x[i] = 1    
#     return x
# string = "hello"
# print(count_characters(string))
