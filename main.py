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
    def __init__(self, id, name, supervisions):
        self.id = id
        self.name = name
        self,supervisions = supervisions

        