#!/usr/bin/env python3

class Student:


 def __init__(self, name, number):
  self.name = name #this will assisgn the students name
  self.number = number #this will assign the number of student
  self.courses = {} #this will start with empty list to store the courses and grade.

 def displayStudent(self): #this function is to display the student details
  return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + str(self.number) #this is the format ostring with the detailedi nformation of student

 def addGrade(self, course, grade): #this function is for our method to add the course with their grade
  self.courses[course] = grade #this is to add the course and grade to the courses list

 def displayGPA(self):
  gpa = 0.0 #this is to start the gpa at 0.0


  if len(self.courses) > 0: # thi sis to check if student has any courses recorded this will be given at the end of script
   for course in self.courses.keys():  #this is loop for all their courses and grade
    gpa = gpa + self.courses[course] #this will be the sum of each course for GPA accumulator


   return 'GPA of student ' + self.name + ' is ' + str(gpa / len(self.courses)) #this is the to calculate average GPA
  return 'GPA of student ' + self.name + ' is 0.0' #if no courses, it will return 0.0 for that GPA of the student

 def displayCourses(self):

  courses_passed = [course for course, grade in self.courses.items() if grade != 0.0] #this is to create the list of courses where grade isnt 0.0 so the passed ones
  return courses_passed #this is to return list of those passed ones.


if __name__ == '__main__':

 #This is going to be object for Student john as student 1
 student1 = Student('John', '013454900')
 student1.addGrade('uli101', 1.0)
 student1.addGrade('ops245', 2.0)
 student1.addGrade('ops445', 3.0)


 #This is going to be object 2 for student Jessica as student 2
 student2 = Student('Jessica', 123456)
 student2.addGrade('ipc144', 4.0)
 student2.addGrade('cpp244', 3.5)
 student2.addGrade('cpp344', 0.0)


 print(student1.displayStudent()) #this isdisplaying student 1 John
 print(student1.displayGPA())
 print(student1.displayCourses())

 print(student2.displayStudent()) #this is displaying student 2 jessica
 print(student2.displayGPA())
 print(student2.displayCourses())


