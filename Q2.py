"""
Name:UKHUREBOR OSAGIE NATHANIEL
StudentID:MSE0103

---------------------------
Question 2:

Write a program in the python programming language using object-oriented programming techniques.
The program enters a list of students, each with information on name, age and test scores.
Sort students by name and order in the alphabet table.
Print the list of students before and after the sorting.

"""
# import itemgetter to sort by the string name using keys
from operator import itemgetter

# import pandas to have the data in a tabular structure
import pandas as pd

class Students:

    number_of_students = 0

    Student_list = []

    def __init__(self, name, age, test_score):

        self.name = name
        self.age = age
        self.test_score = test_score

        # increment the Student class anytime a new student is created
        Students.number_of_students += 1

        # append the student details to the student list
        Students.Student_list.append([self.name, self.age, self.test_score])

    @classmethod
    def print_students(cls):
        print(f"There are currently {cls.number_of_students} active students.")
        print(" ")
        print("The list of students before sorting")
        print(" ")
        df = pd.DataFrame.from_records(cls.Student_list, columns=["name", "age", "test_score"])
        print(df)
        print(" ")
        print("List of students After sorting")
        print(" ")
        print(df.sort_values(by=['name'], ascending=True))

# Test our class
Jerry_martins = Students("Bui Vinh", 23, 55)
Kemi_roland = Students("Nguyen Duc Ngoc", 22, 47)
Ade_Martins = Students("Bishop Nathan", 31, 77)
Chima_festus = Students("Chima Festus", 34, 87)
Chinwe_linda = Students("Huyyen Le", 31, 57)
Chika_bede = Students("Lien Nguyen", 33, 66)
Chioma_jesus = Students("Chioma Jesus", 22, 81)

# this answers the question that prints the students before sorting and after sorting
Students.print_students()
