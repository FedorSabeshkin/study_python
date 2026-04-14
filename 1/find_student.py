from typing import Optional

class StudentId:
   studentId: int

   def __init__(self, id: int):
       self.id = id

class Student:
   studentId: StudentId
   name: str

   def __init__(self, studentId: StudentId, name: str):
       self.studentId = studentId
       self.name = name

def find_student_by_id(studentId : StudentId) -> Optional[Student]:
   # выполнение запроса в БД
   # ...
   return Student(studentId, "Петр")



studentId = StudentId(1)

result = find_student_by_id(studentId)

if result:
   print(f"Студент найден: {result.name}")
else:
   print("Студент не найден")

