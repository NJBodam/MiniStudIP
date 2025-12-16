import os
from studis import Student
from studentlist import StudentList

old_directory = os.getcwd()
print("Current Working Directory:", old_directory)
new_directory = '/Users/mac/Downloads/Thonny Scripts/studentData/'
os.chdir(new_directory)
print("Updated Working Directory:", os.getcwd())
files = os.listdir()
print("\n")


# Import all students from UniOlStudents
uniOL = StudentList()
uniOL.importStudents("UniOlStudents.txt")

# Searchs and print data of the student with index 13 (in the Studentlist)
stud_index13 = uniOL.getStudent(13)
print(f"{stud_index13}\n")

# deregisters the student with index 13
uniOL.deRegister(stud_index13.getNo())

# Searchs and print data of the student with index 13 (in the Studentlist)
stud_index13 = uniOL.getStudent(13)
print(f"{stud_index13}\n")

# finds and prints the student with student number 13 (in the Studentlist)
stud_num13 = uniOL.findStudentNo(13)
print(f"{stud_num13}\n")