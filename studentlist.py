from studis import Student
from studis import Student2BA

class StudentList:

    def __init__(self):
        self.studList = []  # sequence, sorted by student number

    def register(self, studi):
        """ insert student studi into the list"""
        self.studList.append(studi)  # student with largest number is at the end

    def getStudent(self, i):
        """ returns the reference to the student at index i """
        return self.studList[i]

    def __str__(self):
        if len(self.studList) == 0 :
            return "No students registered"
        s = "List of all students:\n"
        for studi in self.studList:
            s += str(studi) + "\n"
        return s

    def findStudentNo(self, number):
        """returns the student with number
        binary search as the seq is sorted by student number
        Parameters:
            number: int
        returns:
            Student
            """
        index = self.search(number)
        if index != -1:
            # return the reference to the student with index self.search(self.seq, key
            return self.studList[index]
        else:  # if no such student exists
            return None

    def findStudentName(self, name):
        """finds the student with name
        Parameters:
            name: String
        returns:
            Student """
        index = self.searchName(name)
        if index != -1:
            # return the reference to the student with index self.search(self.seq, key
            return self.studList[index]
        else:  # if no such student exists
            return None

    def deRegister(self, number):
        """removes student with number  from studentList
           adapts the number of all students in the StudentList
           Parameters
           key : int
               number of a student
           returns: None
               index of student with number
        """
        index = self.search(number)
        if index != -1:
            #self.studList[index].leave()  # Student does some last actions before leaving
            stud = self.studList[index]
            del self.studList[index]
            if stud.minor:
                print(f"Student {stud.firstname} {stud.lastname}, formerly studying {stud.major} and {stud.minor}, leaves the university\n")
            else:
                print(f"Student {stud.firstname} {stud.lastname}, formerly studying {stud.major}, leaves the university\n")
        else:
            print(f"No student with number {number}.")

    def search(self, key):
        """binary search for key = student number
           Parameter
           key : int
               student number
           returns: int
               index of student with number key
        """
        left = 0
        right = len(self.studList)
        while right > left:
            m = (right + left) // 2
            stud_no = (self.studList[m]).getNo()
            if key < stud_no:
                right = m
            elif key > stud_no:
                left = m + 1
            else:
                return m
        else:
            return -1

    def searchName(self, name):
        """sequential search for key = studentName
           Parameter
           key : String
               fist + last name of a student
           returns: int
               index of student with name key
        """
        for i in range(len(self.studList)):
            # listname = self.studList[i].getName()
            if name == self.studList[i].getName():
                return i
        return -1

    def importStudents(self, filename):
        """loads students from a txt file
           and sets term attribute
           Parameters
           filename : String
               name or path for txt file
           returns: None
        """
        file = open(filename,"r")
        file.readline() # get rid of the header line
        for line in file:
            s = line.split("\t")
            #print(s)
            if s[4] =="\n": studi = Student(s[0],s[1], s[3])
            elif s[4]=='': studi = Student(s[0],s[1], s[3])
            else:
                if s[4][-1]=="\n": s[4] = s[4][0:-1] # get rid of the \n in the end
                studi = Student2BA(s[0],s[1],s[3],s[4])
            for sem in range(int(s[2])): studi.inc_term()
            self.register(studi)
        file.close()