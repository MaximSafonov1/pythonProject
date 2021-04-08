# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

class Student:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}

  def add_courses(self, course_name):
    self.finished_courses.append(course_name)

  def __str__(self):
    return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.grades}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"


class Mentor:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []
    self.grades = {}


class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in student.grades:
        student.grades[course] += [grade]
      else:
        student.grades[course] = [grade]
    else:
      return 'Ошибка'

  def __str__(self):
    return f"Имя: {self.name}\nФамилия: {self.surname}"



class Lecturer(Mentor):
  def grading_lecturers(self, student, lecturer, course, grade):
    if isinstance(lecturer, Lecturer) and isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]
      else:
        lecturer.grades[course] = [grade]
    else:
      return 'Ошибка'

  def __str__(self):
    return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grades}"

ruoy = Student('Ruoy', 'Eman', 'male')
ruoy.courses_in_progress += ['Python']
ruoy.courses_in_progress += ['Git']
ruoy.finished_courses += ['Введение в программирование']
print(f'Информация о студенте {ruoy.name}:\n', ruoy)

clark = Student('Clark', 'Kent', 'male')
clark.courses_in_progress += ['Python']
clark.courses_in_progress += ['Git']
clark.finished_courses += ['Введение в программирование']
print(f'\nИнформация о студенте {clark.name}:\n', clark)

sam = Reviewer('Sam', 'Raimi')
sam.courses_attached += ['Python']
sam.rate_hw(ruoy, 'Python', 10)
print(f'\nИнформация о проверяющем {sam.name}:\n', sam)

john = Lecturer('John', 'Konstantin')
john.courses_attached += ['Python']
john.grading_lecturers(ruoy, john, 'Python', 10)
john.grading_lecturers(ruoy, john, 'Python', 10)
print(f'\nИнформация о лекторе {john.name}:\n', john)

sirius = Lecturer('Sirius', 'Black')
sirius.courses_attached += ['Python']
sirius.grading_lecturers(ruoy, sirius, 'Python', 10)
print(f'\nИнформация о лекторе {sirius.name}:\n', sirius)
print(sirius.grades)
