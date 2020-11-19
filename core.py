class User():
    ## Protected
    _name = None
    _regid = None
    _books = []
    _bookLimit = 0
    _fines = 0
    _returnPeriod = 0
    def __init__(self,name):
        self._name = name

    def setRegistrationId(self,registrationID):
        self._regid = registrationID

    def getRegistrationId(self):
        return self._regid

    def getName(self):
        return self._name
    def borrowBook(self,book):
        if len(self._books) < self._bookLimit:
            self._books.append(book)
            return True
        else:
            print('Book Limit Exceeded, Cannot borrow books more than ',self._bookLimit)
            return False

    def returnBook(self,book):
        self._books.remove(book)
        print("book Returned")
        return book
    def getReturnPeriod(self):
        return self._returnPeriod
    def getId(self): ## Abstract method
        raise NotImplementedError

class Student(User): #Inheritence
    _rollno = ''
    _bookLimit = 5
    _returnPeriod = 3
    _lateFine = 1
    def __init__(self,name,rollno):
        self._name = name
        self._rollno = rollno
    def getRollNo(self):
        return self._rollno
    
    def getId(self):    #Polymorphism 
        return self.getRollNo()
    def calculateFine(self,period):
        if period <= self._returnPeriod:
            fine = 0
            return 0
        else:
            fine = (period - self._returnPeriod)* self._lateFine
            self._fines+= fine
            return fine
class Teacher(User):    #Inheritence 
    _employeeID = ''
    _bookLimit = 10
    _returnPeriod = 7
    _lateFine = 0
    def __init__(self,name,employeeID):
        self._name = name
        self._employeeID =employeeID
    def getEmployeeID(self):
        return self._employeeID

    def getId(self):
        return self.getEmployeeID()
    def calculateFine(self,period):
        if period <= self._returnPeriod:
            return 0
        else:
            return 0 ## No late fines for teachers
class Library():
    ## Private
    """
    OOP Best Design practice is make everything private and allow public view via getter and setter methods. 
    This prevents mishandling of data. Use:  Certain object values can be get by Public but cannot be set by public
    """
    __users= {}
    __books = ["Fundamentals of Wavelets","Data Smart","God Created the Integers","Superfreakonomics","Orientalism","Nature of Statistical Learning Theory, The","Integration of the Indian States","Drunkard's Walk, The","Image Processing & Mathematical Morphology","How to Think Like Sherlock Holmes","Data Scientists at Work","Slaughterhouse Five","Birth of a Theorem","Structure & Interpretation of Computer Programs","Age of Wrath, The","Trial, The","Statistical Decision Theory'","Data Mining Handbook","New Machiavelli, The","Physics & Philosophy","Making Software","Analysis, Vol I","Machine Learning for Hackers","Signal and the Noise, The","Python for Data Analysis","Introduction to Algorithms","Beautiful and the Damned, The","Outsider, The","Complete Sherlock Holmes, The - Vol I","Complete Sherlock Holmes, The - Vol II","Wealth of Nations, The","Pillars of the Earth, The","Mein Kampf","Tao of Physics, The","Surely You're Joking Mr Feynman","Farewell to Arms, A","Veteran, The","False Impressions","Last Lecture, The","Return of the Primitive","Jurassic Park","Russian Journal, A","Tales of Mystery and Imagination","Freakonomics","Hidden Connections, The","Story of Philosophy, The","Asami Asami","Journal of a Novel","Once There Was a War","Moon is Down, The","Brethren, The","In a Free State","Catch 22","Complete Mastermind, The","Dylan on Dylan","Soft Computing & Intelligent Systems","Textbook of Economic Theory","Econometric Analysis","Learning OpenCV","Data Structures Using C & C++","Computer Vision, A Modern Approach","Principles of Communication Systems","Let Us C","Amulet of Samarkand, The","Crime and Punishment","Angels & Demons","Argumentative Indian, The","Sea of Poppies","Idea of Justice, The","Raisin in the Sun, A","All the President's Men","Prisoner of Birth, A","Scoop!","Ahe Manohar Tari","Last Mughal, The","Social Choice & Welfare, Vol 39 No. 1","Radiowaril Bhashane & Shrutika","Gun Gayin Awadi","Aghal Paghal","Maqta-e-Ghalib","Beyond Degrees","Manasa","India from Midnight to Milennium","World's Greatest Trials, The","Great Indian Novel, The","O Jerusalem!","City of Joy, The","Freedom at Midnight","Winter of Our Discontent, The","On Education","Free Will","Bookless in Baghdad","Case of the Lame Canary, The","Theory of Everything, The","New Markets & Other Essays","Electric Universe","Hunchback of Notre Dame, The","Burning Bright","Age of Discontuinity, The","Doctor in the Nude","Down and Out in Paris & London","Identity & Violence","Beyond the Three Seas","World's Greatest Short Stories, The","Talking Straight","Maugham's Collected Short Stories, Vol 3","Phantom of Manhattan, The","Ashenden of The British Agent","Zen & The Art of Motorcycle Maintenance","Great War for Civilization, The","We the Living","Artist and the Mathematician, The","History of Western Philosophy","Selected Short Stories","Rationality & Freedom","Clash of Civilizations and Remaking of the World Order","Uncommon Wisdom","One","Karl Marx Biography","To Sir With Love","Half A Life","Discovery of India, The","Apulki","Unpopular Essays","Deceiver, The","Veil: Secret Wars of the CIA","Char Shabda","Rosy is My Relative","Moon and Sixpence, The","Political Philosophers","Short History of the World, A","Trembling of a Leaf, The","Doctor on the Brain","Simpsons & Their Mathematical Secrets","Pattern Classification","From Beirut to Jerusalem","Code Book, The","Age of the Warrior, The","Final Crisis","Killing Joke, The","Flashpoint","Batman Earth One","Crisis on Infinite Earths","Numbers Behind Numb3rs, The","Superman Earth One - 1","Superman Earth One - 2","Justice League: Throne of Atlantis","Justice League: The Villain's Journey","Death of Superman, The","History of the DC Universe","Batman: The Long Halloween","Life in Letters, A","Information, The","Journal of Economics, vol 106 No 3","Elements of Information Theory","Power Electronics - Rashid","Power Electronics - Mohan","Neural Networks","Grapes of Wrath, The","Vyakti ani Valli","Statistical Learning Theory","Empire of the Mughal - The Tainted Throne","Empire of the Mughal - Brothers at War","Empire of the Mughal - Ruler of the World","Empire of the Mughal - The Serpent's Tooth","Empire of the Mughal - Raiders from the North","Mossad","Jim Corbett Omnibus","20000 Leagues Under the Sea","Batatyachi Chal","Hafasavnuk","Urlasurla","Pointers in C","Cathedral and the Bazaar, The","Design with OpAmps","Think Complexity","Devil's Advocate, The","Ayn Rand Answers","Philosophy: Who Needs It","World's Great Thinkers, The","Data Analysis with Open Source Tools","Broca's Brain","Men of Mathematics","Oxford book of Modern Science Writing","Justice, Judiciary and Democracy","Arthashastra, The","We the People","We the Nation","Courtroom Genius, The","Dongri to Dubai","History of England, Foundation","City of Djinns","India's Legal System","More Tears to Cry","Ropemaker, The","Angels & Demons","Judge, The","Attorney, The","Prince, The","Eyeless in Gaza","Tales of Beedle the Bard","Girl with the Dragon Tattoo","Girl who kicked the Hornet's Nest","Girl who played with Fire","Batman Handbook","Murphy's Law","Structure and Randomness","Image Processing with MATLAB","Animal Farm","Idiot, The","Christmas Carol, A"]
    __lentBooks = {}
    __time = 0
    __duePeriod = 3

    def addUser(self,user):
        regNo = 'STD_'+str(user.getId()) + user.getName()[:2]
        if regNo not in self.__users:
            user.setRegistrationId(regNo)
            self.__users[regNo] = []
        else:
            print('User is already registered')
    def _getCurrentTime(self):
        return self.__time
    def increaseTime(self):
        self.__time += 1
    def borrowBook(self,book,user):
        regId = user.getRegistrationId()
        if regId == None:
            print('User is not Registered to the system, ',user.getName())
            return False
        if book not in self.__books:
            print('Book: '+ book +' is not available in our system')
            return False
        if book not in self.__lentBooks:
            status = user.borrowBook(book)
            if status == False:
                print('Cannot lend book to user: ',user.getName())
                return False
            else:
                self.__lentBooks[book] = {'user': regId , 'time':self._getCurrentTime()}
                self.__users[regId].append((book,self._getCurrentTime()))
                print('Book: "'+ book +'" is lent to user: ',user.getName())
                return True
        else:
            print('Book "'+ book + '" cannot be borrowed since its lent to someone else')
            return False
    def returnBook(self,book,user):
        if book not in self.__books:
            print('Book: "'+ book + '" is not available in our system, check again')
            return False
        else:
            regId = user.getRegistrationId()
            if regId == None:
                print('User is not registered to our system')
                return False
            if book not in self.__lentBooks:
                print('Book "{}" is currently not lent to anyone, check again'.format(book))
            else:
                details = self.__lentBooks[book]
                if details["user"] != regId:
                    print('Book "{}" must be returned by original borrower'.format(book))
                else:
                    period = self._getCurrentTime() - details["time"]
                    fines = user.calculateFine(period)
                    if fines != 0:
                        print('User: "{}" is charged {} rupees as late fines. Book taken at {} , returned at {}. Excess days: {}'.format(user.getName(),fines,details["time"],self._getCurrentTime(),period - user.getReturnPeriod()))
                    user.returnBook(book)
                    del(self.__lentBooks[book])
                    return True
                    

            
