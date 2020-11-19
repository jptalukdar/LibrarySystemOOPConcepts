from core import Student,Teacher,Library

library = Library()

mark = Student('mark','CS0001') #Student roll [dept_code]\d\d\d\d
shawn = Teacher('shawn','0004TS') #Teacher roll \d\d\d\dTS

library.addUser(mark)
library.addUser(shawn)

library.borrowBook('BookName',mark) #Failure since book not exists
library.borrowBook("Data Smart",mark) #Success mark - 1
library.increaseTime() ## For days simulation
library.borrowBook("Data Smart",mark) #Failure since already borrowed
library.returnBook('BookName',shawn) #Failure since he didn't take that book

library.borrowBook("Catch 22",mark) #Success mark - 1
library.increaseTime()
library.borrowBook("In a Free State",mark) #Success mark - 1
library.increaseTime()
library.increaseTime()
library.borrowBook("God Created the Integers",mark) #Success mark - 1
library.increaseTime()
library.borrowBook("Fundamentals of Wavelets",mark) #Success mark - 1
library.increaseTime()
library.borrowBook("Beyond the Three Seas",mark) #Failure mark - 5 since 
library.increaseTime()
library.returnBook("Data Smart",mark)

library.borrowBook("Data Smart",shawn)
