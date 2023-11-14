# Encontrar al segundo mejor estudiante
class Student:
    def __init__(self, name, score):
        self.name=name
        self.score=score
# Tupla con estudiantes y sus notas
tupla_student=[["carlos",5.1],["elias",5.1],["joeni",5.2],["joana",5.4],["juana",20.1]]
record=list()
# Creacion de lista de objetos estudiantes
for student in tupla_student:
    record.append(Student(student[0],student[1]))
# lista ordernada por el atributo score
record.sort(key=lambda student : student.score)
second_place=list()
lower_student=record[0]
aux_student=Student("Aux", 0)
# 1,2,3,4,5
for student_object in record:
    if student_object.score > lower_student.score:
        aux_student.name=student_object.name
        aux_student.score=student_object.score
        break
for student_object in record:
    if student_object.score == aux_student.score:
        second_place.append(student_object)
#Ordenar por el atributo nombre
second_place.sort(key=lambda student : student.score)
for student in second_place:
    print(student.name)

