#1)
a = input("Введите число 1:")
b = input("Введите число 2:")
d = int(b) + 1
c = sum(range(int(a), int(d)))
print("Результат:", c)
print()

#2)
numbers = []

print("Введите данные по одному.")

while True:
    user_input = input("Введите данные: ")
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        break

if numbers:
    min_value = min(numbers)
    max_value = max(numbers)
    print(f"Минимальное значение: {min_value}")
    print(f"Максимальное значение: {max_value}")
else:
    print("Вы не ввели ни одного числа.")
print()

#3)
from statistics import mean
students = [
        ('Александр', 'Терещенко', [90, 85, 92], [88, 79, 95], 0.80),
        ('Владимир', 'Царев', [60, 70, 65], [75, 72, 78], 0.90),
        ('Елена', 'Симакова', [100, 95, 98], [90, 92, 94], 0.74),
        ('Анжелика', 'Копухина', [88, 91, 85], [89, 85, 87], 0.97),
        ('Виктор', 'Сухоруков', [70, 68, 73], [69, 71, 70], 0.60),
    ]

print("Студенты с посещаемостью ниже 75%:")
for name, surname, py, math, attend in students:
    if attend < 0.75:
        print(f'  {name} {surname} — {attend:.0%}')
print() 

best_student = None
best_avg = -1

for student in students:
    name,surname,python_grades, math_grades, attendance = students
    
    avg_python = sum(python_grades)/len(python_grades)
    avg_math = sum(math_grades)/len(math_grades)
    overall_avg = (avg_python + avg_math)/2
        if overall_avg > best_avg:
            best_avg = overall_avg
            best_student = student
print("\nЛучший студент: ")

if best_student:
    print(f"{best_student[0]}{best_student[1]}")

for name, surname, py, math, _ in students:
    if mean(py) < mean(math):
        print(f"{name} {surname} нужно уделить больше внимания Python!")
print()


