class User():
    ## Protected
    _name = ''
    _regid = ''
    _books = []
    _bookLimit = 0
    def __init__(self,name):
        self._name = name

    def setRegistrationId(self,registrationID):
        self._regid = registrationID
    
    def borrowBook(self,book):
        if len(self._books) < self._bookLimit:
            self._books.append(book)
        else:
            print('Book Limit Exceeded, Cannot borrow books more than ',self._bookLimit)

    def returnBook(self,book):
        self._books.remove(book)
        print("book Returned")
        return book

class Student(User):
    _rollno = ''
    _bookLimit = 5
    def __init__(self,name,rollno):
        self._name = name
        self._rollno = rollno
    def getRollNo(self):
        return self._rollno

class Teacher(User):
    _employeeID = ''
    _bookLimit = 10
    def __init__(self,name,employeeID):
        self._name = name
        self._employeeID =employeeID
    def getEmployeeID(self):
        return self._employeeID

class Library():
    __students = {}
    __teachers = {}
    __books = []
    __lentBooks = {}
    def addStudent(self,student):
        regNo = 'STD_'+str(student.getRollNo()) + student.getName()[:2]
        if regNo not in self.__students:
            student.setRegistrationId(regNo)
            self.__students[regNo] = []
        else:
            print('Student is already registered')

    def addTeacher(self,teacher):
        regNo = 'TEC_'+str(teacher.getEmployeeID()) + teacher.getName()[:2]
        teacher.setRegistrationId(regNo)
        if regNo not in self.__teachers:
            self.__teachers[regNo] = []
    def borrowBook(self,book,user):
        if type(user) == type(Student):
            self.__borrowBookStudent(book,user)
        elif type(user) == type(Teacher):
            self.__borrowBookTeacher(book,user)
    def __borrowBookStudent(self,book,user):
        pass
    def __borrowBookTeacher(self,book,user):
        pass
    def __returnBookStudent(self,book,user):
        pass
    def __returnBookTeacher(self,book,user):
        pass
    def returnBook(self,book,user):
        if type(user) == type(Student):
            self.__returnBookStudent(book,user)
        elif type(user) == type(Teacher):
            self.__returnBookTeacher(book,user)