class Employee:
    # information
    def __init__(self, fio, salary, stage, level, grade, status):
        self.status = status  # статус
        self._fio = fio  # фио
        self._salary = salary  # рубли
        self._stage = stage  # месяц
        self._level = level  # уровень
        self._grade = grade  # должность
        self.__prize = False  # премия

    # получить
    def get_clear__salary(self):  # получить зарплату чистыми
        clear__salary = round(self._salary * 0.8)
        if self.__prize:
            clear__salary += 10000
        print(f"{clear__salary}$")

    def get_info(self):  # получить информацию
        print(f"Status - {self.status}\nName - {self._fio}\n  Salary - {self._salary}$\n"
              f"  Stage - {self._stage} Month\n  Level - {self._level}\n"
              f"  Grade - {self._grade}")
        if self.__class__ != Hired:
            print(f"  Prize - {self.__prize}\n")

    # изменить
    def set_grade(self):
        old_grade = self._grade
        new_grade = input(f"* To get back enter clear string\nInput new _grade: ")
        if new_grade != "":
            if new_grade != old_grade:
                self._grade = new_grade
                print(f"{old_grade} grade of {self._fio} was changed to {self._grade}")
            else:
                print(f"{self._grade} grade of {self._fio} wasn't changed")

    # выдать
    def __give_prize(self):  # give prize | protected function
        self.__prize = True
        print(f"prem for {self._fio} was gived")


class Hired(Employee):
    def __init__(self, fio, salary, stage, level, grade, company, hired_time, status):
        Employee.__init__(self, fio, salary, stage, level, grade, status)
        self.__company = company  # protected
        self.__hired_time = hired_time  # protected

    def get_info(self):
        Employee.get_info(self)
        print(f"  Company - {self.__company}\n  Hired for {self.__hired_time} month\n")


emp_1 = Employee("Omega Dreemurr", 2000, 64, "Senior", "Manager", "Employer")
emp_2 = Employee("Ivanov Ivan", 1350, 35, "Middle", "Team Leader", "Employer")
emp_3 = Employee("Simonov Dmitryi", 900, 13, "Junior", "C++ Devoleper", "Employer")
emp_4 = Hired("Kornev Roman", 900, 12, "Junior", "Py Devoleper", "Alpha", "24", "Hired")
emp_5 = Hired("Joseph Jostar", 900, 11, "Junior", "Js Devoleper", "Delta", "12", "Hired")
