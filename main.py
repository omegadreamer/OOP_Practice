class Employee:
    # information
    def __init__(self, fio, salary, stage, level, grade):
        self.fio = fio  # фио
        self.salary = salary  # рубли
        self.stage = stage  # месяц
        self.level = level  # уровень
        self.grade = grade  # должность
        self.__prize = False  # премия

    # получить
    def get_clear_salary(self):  # получить зарплату чистыми
        clear_salary = round(self.salary * 0.8)
        if self.__prize:
            clear_salary += 10000
        print(f"{clear_salary}$")

    def get_info(self):  # получить информацию
        print(f"Name - {self.fio}\n  Salary - {self.salary}$\n"
              f"  Stage - {self.stage} Month\n  Level - {self.level}\n"
              f"  Grade - {self.grade}")
        if self.__class__ != Hired:
            print(f"  Prize - {self.__prize}\n")

    # изменить
    def set_grade(self):
        old_grade = self.grade
        new_grade = input(f"* To get back enter clear string\nInput new grade: ")
        if new_grade != "":
            if new_grade != old_grade:
                self.grade = new_grade
                print(f"{old_grade} grade of {self.fio} was changed to {self.grade}")
            else:
                print(f"{self.grade} grade of {self.fio} wasn't changed")

    # выдать
    def __give_prize(self):  # give prize | protected function
        self.__prize = True
        print(f"prem for {self.fio} was gived")


class Hired(Employee):
    def __init__(self, fio, salary, stage, level, grade, company, hired_time):
        Employee.__init__(self, fio, salary, stage, level, grade)
        self.__company = company  # protected
        self.__hired_time = hired_time  # protected

    def get_info(self):
        print(f"Company - {self.__company}\nHired for {self.__hired_time} month")
        Employee.get_info(self)
        print(f"\n")


emp_1 = Employee("Omega Dreemurr", 2000, 64, "Senior", "Manager")
emp_2 = Employee("Ivanov Ivan", 1350, 35, "Middle", "Team Leader")
emp_3 = Employee("Simonov Dmitryi", 900, 13, "Junior", "C++ Devoleper")
emp_4 = Hired("Kornev Roman", 900, 12, "Junior", "Py Devoleper", "Alpha", "24")
emp_5 = Hired("Joseph Jostar", 900, 11, "Junior", "Js Devoleper", "Delta", "12")

emp_1.get_info()
emp_4.get_info()
