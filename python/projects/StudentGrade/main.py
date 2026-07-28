from student_model import Student
from data import data
from report_card import ReportCard

student_list=[]
for student in data:
    student_name=student["name"]
    student_marks=student["marks"]
    student_record=Student(student_name,student_marks)
    student_list.append(student_record)
report_data=ReportCard(student_list)

while report_data.has_next_students():
    report_data.show_student()
print("Students list ends!")