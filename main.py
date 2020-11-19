from core import Student,Teacher,Library

library = Library()
student = Student('abc')
library.addStudent(student)
library.addTeacher(Teacher('xyz'))

library.borrowBook('BookName',student)
library.returnBook('BookName',student)