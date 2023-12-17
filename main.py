lessons = open('lessons.csv', 'r')
supervisors = open('supervisors.csv', 'r')

class Course:
    def __init__(self, id, title, date_time, exam_room, supervisors_needed, professor, semester):
        self.id = id
        self.title = title
        self.date_time = date_time
        self.exam_room = exam_room
        self.supervisors_needed = supervisors_needed
        self.professor = professor
        self.semester = semester

class Supervisor:
    def __init__(self, id, name, supervisions, unavailabilities):
        self.id = id
        self.name = name
        self.supervisions = supervisions
        self.unavailabilities = unavailabilities

def assign(courses, supervisors):
    assigned = list()
    for course in courses:
        available_sups = [Supervisor for Supervisor in supervisors if Course.id not in Supervisor.unavailabilities]
        for i in range(Course.supervisors_needed):
            if len(available_sups) == 0:
                break
            assigned_sup = available_sups.pop(0)
            assigned_sup.supervisions -= 1
            assigned.append(assigned.id)
    return assigned




        