from datetime import datetime
class Student:
    def __init__(self, name, grades):
        self.name = name
        self._enrollments = []
        self.grades = {}

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")
        
    def aggregate_average_grade(self):
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        average_grade = total_grades / num_courses
        return average_grade    

    def get_enrollments(self):
        return self._enrollments.copy()

class Course:
    def __init__(self, title):

        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()


class Enrollment:
    all = []
    
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date
