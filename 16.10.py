numbers = [1, 2, 3, 4, 5]

people = ["Tom", "Sam", "Bob"]
numbers1 = []
numbers2 = list()

objects = [1, 2.6, "Hello", True]
numbers = [1, 2, 3, 4, 5]
people = ["Tom", "Sam", "Bob"]
print(numbers)  # [1, 2, 3, 4, 5]
print(people)  # ["Tom", "Sam", "Bob"]

numbers1 = [1, 2, 3, 4, 5]
numbers2 = list(numbers1)
print(numbers2)  # [1, 2, 3, 4, 5]

letters = list("Hello")
print(letters)  # ['H', 'e', 'l', 'l', 'o']

numbers = [5] * 6  # 6 раз повторяем 5
print(numbers)  # [5, 5, 5, 5, 5, 5]

people = ["Tom"] * 3  # 3 раза повторяем "Tom"
print(people)  # ["Tom", "Tom", "Tom"]

students = ["Bob", "Sam"] * 2  # 2 раза повторяем "Bob", "Sam"
print(students)  # ["Bob", "Sam", "Bob", "Sam"]

people = ["Tom", "Sam", "Bob"]
# получение элементов с начала списка
print(people[0])  # Tom
print(people[1])  # Sam
print(people[2])  # Bob

# получение элементов с конца списка
print(people[-2])  # Sam
print(people[-1])  # Bob
print(people[-3])  # Tom

people = ["Tom", "Sam", "Bob"]

people[1] = "Mike"  # изменение второго элемента
print(people[1])  # Mike
print(people)  # ["Tom", "Mike", "Bob"]

people = ["Tom", "Bob", "Sam"]

tom, bob, sam = people

print(tom)  # Tom
print(bob)  # Bob
print(sam)  # Sam