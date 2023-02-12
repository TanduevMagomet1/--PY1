class Employee:
    ''' Базовый класс "Сотрудники компании" '''

    def __init__(self, work_experience: int, specialisation: str):
        """
        Создание и подготовка к раоте объекта "Сотрудник компании"
        :param work_experience: Опыт работы
        :param specialisation: Специализация

        Примеры:
        >>> employee_1 = Employee(20, "Архитектор")
        """
        if not isinstance(work_experience, int):
            raise TypeError("Опыт работы должен быть типа int")
        self.work_experience = work_experience

        if not isinstance(specialisation, str):
            raise TypeError("Специализация сотрудника должен быть типа str")
        self.specialisation = specialisation

    def __str__(self):
        return f"Опыт работы {self.work_experience}. Специализация {self.specialisation}"

    def __repr__(self):
        return f"{self.__class__.__name__}(specialisation = {self.specialisation!r}, work_experience = {self.work_experience!r})"

    def salary(self) -> int:
        """
        Функция которая считает зарплату сотрудника

        Примеры:
        >>> employee_1 = Employee(20, "Архитектор")
        >>> employee_1.salary()
        """
        ...

    def partner(self) -> bool:
        """
        Функция которая определяет может ли сотрудник стать партнером компании

        :return: Может стать партнером или нет

        Примеры:
        >>> employee_1 = Employee(20, "Архитектор")
        >>> employee_1.partner()
        """
        ...


class Engineer(Employee):
    def __init__(self, work_experience: int, specialisation: str, category: int):
        """
        Cоздание и подготовка к раоте объекта "Инженер-конструктор"
        :param work_experience: Опыт работы
        :param specialisation: Специализация
        :param category: Категоря

        Примеры:
        >>> employee_1 = Employee(20, "Инженер-конструктор", 1)
        """
        super().__init__(work_experience, specialisation)

        if not isinstance(category, int):
            raise TypeError("Категория инженера-конструктора должена быть типа int")
        if category < 0 or category >3:
            raise TypeError("Категория инженера-конструктора должена быть больше 0 и не может быть больше 3")
        self.category = category

    def salary(self) -> int:

        super().salary()
        """
        Функция которая считает зарплату сотрудника
        """
        ...

    def partner(self, category) -> bool:
        """
        Функция которая определяет может ли сотрудник стать партнером компании

        :return: Может стать партнером или нет
        """
        if category > 1:
            return False

    def __str__(self):
        return f"Опыт работы {self.work_experience}. Специализация {self.specialisation}. Категория {self.category}"

    def __repr__(self):
        return f"{self.__class__.__name__}(specialisation = {self.specialisation!r}, work_experience = {self.work_experience!r}), category = {self.category!r}


if __name__ == "__main__":
    pass
