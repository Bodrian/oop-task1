class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.grades_lect()}\nКурсы в процессе обучения: {self.course_str()}\nЗавершенные курсы: {self.course_fin_str()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение не корректно')
            return
        else:
            return self.grades_lect() < other.grades_lect()

    def course_str(self):
        corse_s = ''
        for corse in self.courses_in_progress:
            corse_s += corse
        if corse_s == '':
            corse_s = 'нет курсов в процессе обучения'
        return corse_s

    def course_fin_str(self):
        corse_s = ''
        for corse in self.finished_courses:
            corse_s += corse
        if corse_s == '':
            corse_s = 'нет завершенных курсов'
        return corse_s

    def grades_lect(self):
        sum1 = 0
        len1 = 0
        for grade in self.grades.values():
            sum1 += (sum(grade))
            len1 += len(grade)
        srednee = sum1/len1
        return srednee

    def rate_lect(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.grades_lect()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение не корректно')
            return
        return self.grades_lect() < other.grades_lect()

    def grades_lect(self):
        sum1 = 0
        len1 = 0
        for grade in self.grades.values():
            sum1 += (sum(grade))
            len1 += len(grade)
        srednee = sum1/len1
        return srednee

class Reviewer(Mentor):
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student1 = Student('Ruoy1', 'Eman1', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer2 = Lecturer('Some2', 'Buddy2')
cool_reviewer = Reviewer('Some1', 'Buddy1')
cool_lecturer.courses_attached += ['Python']
cool_lecturer2.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student1, 'Python', 8)
best_student.rate_lect(cool_lecturer, 'Python', 10)
best_student.rate_lect(cool_lecturer, 'Python', 8)
best_student.rate_lect(cool_lecturer2, 'Python', 5)
#cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
print(cool_lecturer.grades)
print(cool_reviewer)
print(cool_lecturer)
print(cool_lecturer2)
print(best_student)

print('Сравнение лекторов')
if cool_lecturer > cool_lecturer2:
    print(f'{cool_lecturer.name} круче {cool_lecturer2.name}')
else:
    print(f'{cool_lecturer2.name} круче {cool_lecturer.name}')

print('Сравнение студентов')
if best_student > best_student1:
    print(f'{best_student.name} круче {best_student1.name}')
else:
    print(f'{best_student1.name} круче {best_student.name}')