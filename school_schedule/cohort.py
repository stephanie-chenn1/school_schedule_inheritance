class Cohort:
    def __init__(self,cohort_name,students=None):
        self.cohort_name = cohort_name
        self.students = students if students is not None else []
        
    def student_summaries(self):
        for student in self.students:
            print(student.summary())
            
    def class_list(self, course_name):
        course_list = []
        for student in self.students:
            if course_name in student.classes:
                course_list.append(student.name)
        return course_list
