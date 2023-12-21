lessons = open('lessons.csv', 'r', encoding='utf8')
supervisors = open('supervisors.csv', 'r', encoding='utf8')

class Course:
    def __init__(self, id, date_time, exam_rooms, semester, professor, supervisors_needed):
        self.id = id
        self.date_time = date_time
        self.exam_rooms = exam_rooms
        self.semester = semester
        self.professor = professor
        self.supervisors_needed = supervisors_needed
        
class Supervisor:
    def __init__(self, id, name, email, supervisions, unavailabilities):
        self.id = id
        self.name = name
        self.email = email
        self.supervisions = supervisions
        self.unavailabilities = unavailabilities

def get_courses_from_csv(lessons):
    #μετατρέπουμε κάθε σειρά του lessons.csv σε αντικείμενο και τα τοποθετούμε στην λίστα courses
    courses = list()
    lessons.readline()
    for line in lessons:
        line = line.strip()
        ls = line.split(',')
        exam = Course(int(ls[0]), ls[1], ls[2], ls[3], ls[4], int(ls[5]))
        courses.append(exam)
    return courses

def get_supervisors_from_csv(supervisors):
    #μετατρέπουμε κάθε σειρά του supervisors.csv σε αντικείμενο και τα τοποθετούμε στην λίστα supervisors
    supervisors = list()
    for line in supervisors:
        ls = line.split(',')
        supervisor = Supervisor(int(ls[0]), ls[1], ls[2], int(ls[3]), ls[4])
        supervisors.append(supervisor)
    return supervisors

def assign(courses, supervisors):
    assigned = list()
    for course in courses:
        available_sups = [supervisor for supervisor in supervisors if str(course.id) not in supervisor.unavailabilities]
        for i in range(course.supervisors_needed):
            if len(available_sups) == 0:
                break
            assigned_sup = available_sups.pop(0)
            assigned.append(assigned_sup)
    return assigned





        