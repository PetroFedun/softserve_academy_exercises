# Your task is to write a program which allows teachers to create a multiple choice test 
# in a class called Testpaper and to be also able to assign a minimum pass mark. 
# The testpaper's subject should also be included. 
# The attributes are in the following order:
# 1. subject
# 2. markscheme
# 3. pass_mark
# As well as that, we need to create student objects to take the test itself! Create another class called Student and do the following:
# Create an attribute called tests_taken and set the default as  'No tests taken'.
# Make a method called take_test(), which takes in the testpaper object they are completing and the student's answers. Compare what they wrote to the mark scheme, and append to the/create a dictionary assigned to tests_taken in the way as shown in the point below.
# Each key in the dictionary should be the testpaper subject and each value should be a string in the format seen in the examples below (whether or not the student has failed, and their percentage in brackets).
# Example:
# paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
# paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
# paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")
# student1 = Student()
# student2 = Student()
# student1.tests_taken ➞ "No tests taken"
# student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
# student1.tests_taken ➞ {"Maths" : "Passed! (80%)"}
# student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
# student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
# student2.tests_taken ➞ {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}

import math

class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark
        
class Student:
    tests_taken =  "No tests taken"

    def take_test(self, testpaper, answers):
        subject = testpaper.subject
        markscheme = testpaper.markscheme
        pass_mark = float(testpaper.pass_mark.rstrip('%'))

        if len(answers) == len(markscheme):
            score = sum([1 for student_ans, correct_ans in zip(answers, markscheme) if student_ans == correct_ans])
            percentage = (score / len(markscheme)) * 100
            result = "Passed!" if percentage >= pass_mark else "Failed!"
            result_str = f"{result} ({math.ceil(percentage)}%)"
            
            if self.tests_taken == "No tests taken":
                self.tests_taken = {subject: result_str}
            else:
                self.tests_taken[subject] = result_str
        else:
            print("Number of answers does not match the number of questions.")

paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")
student1 = Student()
student2 = Student()
assert student1.tests_taken == "No tests taken"
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
assert student1.tests_taken == {"Maths" : "Passed! (80%)"}
student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
assert student2.tests_taken == {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}


