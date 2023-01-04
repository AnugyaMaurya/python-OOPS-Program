#Write a Python program to demonstrate multiple inheritance.
'''1. Employee class has 3 data members EmployeeID, Gender (String), Salary and
PerformanceRating(Out of 5) of type int. It has a get() function to get these details from
the user.
2. JoiningDetail class has a data member DateOfJoining of type Date and a function
getDoJ to get the Date of joining of employees.
3. Information Class uses the marks from Employee class and the DateOfJoining date
from the JoiningDetail class to calculate the top 3 Employees based on their Ratings
and then Display, using readData, all the details on these employees in Ascending
order of their Date Of Joining.'''

import datetime as dt


class Employee:
    def __init__(self, id: str, gender: str, salary: int, perfomance_rating: int):
        self.id, self.gender, self.salary, self.perfomance_rating = id, gender, salary, perfomance_rating

    def get_id(self):
        return self.id

    def get_gender(self):
        return self.gender

    def get_salary(self):
        return self.salary

    def get_perf_rat(self):
        return self.perfomance_rating


class JoiningDetail(Employee):
    def __init__(self, id: str, gender: str, salary: int, perfomance_rating: int, date: dt.date):
        super().__init__(id, gender, salary, perfomance_rating)
        self.date = date

    def get_DoJ(self):
        return self.date

    def __str__(self):
        return f"id {self.id} : {self.date}"


class Information(Employee):
    def __init__(self, e_list):
        self.e_list = e_list

    def readData(self):
        N = len(self.e_list)
        for i in range(N - 1):
            for j in range(N - i - 1):
                if self.e_list[j].get_perf_rat() > self.e_list[j + 1].get_perf_rat():
                    self.e_list[j], self.e_list[j + 1] = self.e_list[j + 1], self.e_list[j]

        for i in range(3):
            for j in range(2 - i):
                if self.e_list[j].get_DoJ() > self.e_list[j + 1].get_DoJ():
                    self.e_list[j], self.e_list[j + 1] = self.e_list[j + 1], self.e_list[j]

        return '\n'.join(list(map(str, self.e_list[:3])))
obj=Employee(4,"F",200000,5)
obj.get_salary()
obj1=JoiningDetail(4,"F",200000,5,2020)
obj1.get_DoJ()