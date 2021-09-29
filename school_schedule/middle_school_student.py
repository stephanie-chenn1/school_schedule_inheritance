from .student import Student

class Middle_School_Student(Student): 
    def __init__(self, name, grade, classes, gets_transportation = False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation
