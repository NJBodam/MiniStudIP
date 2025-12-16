class Student:
    number = 0  # Class variable: maximum of ALL current Student numbers

    def __init__(self, fname, lname, major, t = 1):
        """ Constructor of Student objects, initializes a new student with name
        study subject (major), a unique student number and sets its term to 1
        Parameters:
        fname, lname: String
            First and last name of a new student
        major: String
            study programme of the student
        returns:
            reference to the new student object
        """
        self.firstname = fname
        self.lastname = lname
        self.major = major
        Student.number += 1  # next Student.number
        self.num = Student.number  # next free number
        self.term = t  # Student is a fresh(wo)man

    def __str__(self):
        # return a nice printable version of a Student
        # {self.num:3} enforces that self.num will printed with 3 chars
        return f"{self.num:3}: {self.firstname} {self.lastname} studies {self.major} in her/his {self.term} Semester."

    def getName(self):
        return self.firstname + " " + self.lastname

    def getLastFirstName(self):
        return self.lastname + ", " + self.firstname

    def getSubject(self):
        return self.major

    def getNo(self):
        return self.num

    def getTerm(self):
        return self.term

    def inc_term(self):
        """increments the attribute term by 1 """
        self.term += 1

    def setLastName(self, newName):
        self.lastname = newName

    def setMajor(self, newMajor):
        self.major = newMajor

    def setTerm(self, term):
        self.term = term


class Student2BA(Student):
    def __init__(self, fname, lname, major, minor):
        """ Constructor of Student2BA objects, initializes a new 2BA student with name
        study subjects (major and minor), a unique student number and sets its term to 1
        Parameters:
        fname, lname: String
            First and last name of a new student
        major: String
            study programme of the student
        returns:
            reference to the new student object
        """
        Student.__init__(self, fname, lname, major)  # execute the constructor of the superclass Student
        self.setMinor(minor)

    def __str__(self): # OVERWRITE then inherited method
        # construct a nice printable version of a Student
        return f"{self.num:3}: {self.firstname} {self.lastname} studies {self.major} and {self.minor} in her/his " \
               f"{self.term} Semester."

    def setMinor(self, newMinor):
        if self.major == newMinor:
            print("Minor subject must be different from major subject")
        else:
            self.minor = newMinor

    def setMajor(self, newMajor):
        if self.minor == newMajor:
            print("Major subject must be different from minor subject")
        else:
            self.major = newMajor