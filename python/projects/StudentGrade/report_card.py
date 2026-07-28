class ReportCard:
    def __init__(self,student_list):
        self.student_list=student_list
        self.current_student=0
    def has_next_students(self):
        return self.current_student<len(self.student_list)
    def calculate_grade(self):
        student=self.student_list[self.current_student]
        if student.marks>=90:
            return "A"
        elif student.marks<90 and student.marks>=80:
            return "B"
        else:
            return "C"
    def show_student(self):
        student=self.student_list[self.current_student]
        print(f"Student Name: {student.name}")
        print(f"Marks: {student.marks}")
        a=self.calculate_grade()
        print(f"Grade: {a}")
        self.current_student+=1