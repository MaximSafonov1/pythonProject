def average_rating(person):
    if isinstance(person, Lecturer) or isinstance(person, Student):
        summa = 0
        number = 0
        for i in person.grades:
            summa += sum(person.grades[i])
            number += len(person.grades[i])
            return summa / number


def course_average_grade(list_of_persons):
    if isinstance(list_of_persons, list):
        middle = 0
        number = 0
        if isinstance(list_of_persons[0], Student) or isinstance(list_of_persons[0], Lecturer):
            for i in list_of_persons:
                middle += average_rating(i)
                number += 1
        try:
            return middle / number
        except ZeroDivisionError:
            return 0


def get_list_students():
    return Student.all_students


def get_list_lectors():
    return Lecturer.all_lectors


class Student:
    all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.all_students.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def grading_lecturers(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            print("Такого лектора нет.")
        else:
            if course in lecturer.courses_attached:
                try:
                    lecturer.grades[course].append(grade)
                except BaseException:
                    lecturer.grades[course] = [grade]
            else:
                print(f"{lecturer.name} {lecturer.surname} не ведет курс {course}")

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_rating(self)}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"

    def __lt__(self, another_student):
        return average_rating(self) < average_rating(another_student)

    def __le__(self, another_student):
        return average_rating(self) <= average_rating(another_student)

    def __eq__(self, another_student):
        return average_rating(self) == average_rating(another_student)


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
    all_lectors = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.all_lectors.append(self)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_rating(self)}"

    def __lt__(self, another_lecturer):
        return average_rating(self) < average_rating(another_lecturer)

    def __le__(self, another_lecturer):
        return average_rating(self) <= average_rating(another_lecturer)

    def __eq__(self, another_lecturer):
        return average_rating(self) == average_rating(another_lecturer)


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
sam.rate_hw(ruoy, 'Python', 9)
sam.rate_hw(ruoy, 'Python', 10)
sam.rate_hw(clark, 'Python', 9)
sam.rate_hw(clark, 'Python', 9)
sam.rate_hw(clark, 'Python', 10)
print(f'\nИнформация о проверяющем {sam.name}:\n', sam)

john = Lecturer('John', 'Konstantin')
john.courses_attached += ['Python']
ruoy.grading_lecturers(john, 'Python', 8)
clark.grading_lecturers(john, 'Python', 10)
print(f'\nИнформация о лекторе {john.name}:\n', john)

sirius = Lecturer('Sirius', 'Black')
sirius.courses_attached += ['Python']
ruoy.grading_lecturers(sirius, 'Python', 10)
clark.grading_lecturers(sirius, 'Python', 9)
print(f'\nИнформация о лекторе {sirius.name}:\n', sirius)
print()
print(john < sirius)
print(john >= sirius)
print(john == sirius)
print()
print(ruoy > clark)
print(ruoy >= clark)
print(ruoy == clark)
print()
print(round(average_rating(clark), 2))
print(round(average_rating(ruoy), 2))
print()
print(course_average_grade(get_list_students()))
print(course_average_grade(get_list_lectors()))
