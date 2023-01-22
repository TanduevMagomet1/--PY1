# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Wall:
    def __init__(self, volume: float, thickness: float, openings: list[list[int, float, float]]):
        """
       Создание и подготовка к работе объекта "Стена"

       :param volume: Объем стены
       :param thickness: Толщина стены
       :param openings: Список отверстий в стене

       Примеры:
       >>> new_wall = Wall(20000, 200, [[1, 300, 500], [2, 500, 800]])
       """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем стены должен быть типа int или float")
        if volume <= 0:
            raise ValueError("Объем стены должен быть положительным числом")
        self.volume = volume

        if not isinstance(thickness, (int, float)):
            raise TypeError("Толщина стены должена быть типа int или float")
        if volume <= 0:
            raise ValueError("Толщина стены должена быть положительным числом")
        self.thickness = thickness

        if not isinstance(openings, list):
            raise TypeError("Информация об отверстиях подается списком списков типа list,"
                            "с порядковым номером отверстия типа int, высотой и шириной типа int или float")
        self.openings = openings

    def is_have_openings(self) -> bool:
        """
        Функция которая проверяет есть ли в стене отверстия

        :return: Есть ли отверстия в стене

        Примеры:
        >>> new_wall = Wall(20000, 200, [[1, 300, 500], [2, 500, 800]])
        >>> new_wall.is_have_openings()
        """
        ...

    def make_opening(self, height: float, width: float) -> list:
        """
        Функция которая добавляет отверстие в стене и присваивает ему порядковый номер

        :param height: Высота отверстия
        :param width: Ширина отверстия

        :return: Обновленный список отверстий

        Примеры:
        >>> new_wall = Wall(20000, 200, [[1, 300, 500], [2, 500, 800]])
        >>> new_wall.make_opening(500, 200)
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота отверстия должена быть типа int или float")
        if height <= 0:
            raise ValueError("Высота отверстия должена быть положительным числом")

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина отверстия должена быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина отверстия должена быть положительным числом")
        ...

    def patch_opening(self, number: int) -> list:
        """
        Функция которая заделывает отверстие в стене
        :param number: Номер отверстия

        :return: Обновленный список отверстий

        Примеры:
        >>> new_wall = Wall(20000, 200, [[1, 300, 500], [2, 500, 800]])
        >>> new_wall.patch_opening(2)
        """
        if not isinstance(number, int):
            raise TypeError("Номер отверстия должен быть типа int")
        if number <= 0:
            raise ValueError("Номер отверстия должен быть положительным числом")
        ...


class SeatingPlan:
	def __init__(self, number_of_seats: int, number_of_visits: int):
		"""
		Создание и подготовка "Плана рассадки" гостей в ресторане:

		:param number_of_seats: Количество посадочных мест
		:param number_of_visits: Количество посетителей

		Примеры:
		>>> seating = SeatingPlan(500, 300)
		"""
		if not isinstance(number_of_seats, int):
			raise TypeError("Количество посадочных мест должно быть типа int")
		if number_of_seats <= 0:
			raise ValueError("Количество посадочных мест должно быть положительным числом")
		self.number_of_seats = number_of_seats

		if not isinstance(number_of_visits, int):
			raise TypeError("Количество посетителей должно быть типа int")
		if number_of_visits <= 0:
			raise ValueError("Количество посетителей должно быть положительным числом")
		if number_of_visits >= number_of_seats:
			raise ValueError("Количество посетителей должно быть меньше чем число мест")
		self.number_of_visits = number_of_visits

	def available_seats(self) -> int:
		"""
		Определение количества свободных мест.

		:return: Количество свободных мест

		Примеры:
		>>> seating = SeatingPlan(500, 300)
		>>> seating.available_seats()
		"""
		...

	def new_visitors(self, number_of_new_visitors: int) -> None:
		"""
		Добавление новых посетителей.

		:param number_of_new_visitors: Количество новых посетителей

		raise ValueError: Если количество посетителей больше количества свободных посадочных мест

		Примеры:
		>>> seating = SeatingPlan(500, 300)
		>>> seating.new_visitors(50)
		"""

		if not isinstance(number_of_new_visitors, int):
			raise TypeError("Количество новых посетителей должно быть типа int")
		if number_of_new_visitors <= 0:
			raise ValueError("Количество новых посетителей должно быть положительным числом")
		...

	def new_seats(self, number_of_new_seats: int) -> int:
		"""
		Добавление запасных посадочных мест.

		:param number_of_new_seats: Количество новых посадочных мест

		:return: Новое количество посадочных мест

		Примеры:
		>>> seating = SeatingPlan(500, 300)
		>>> seating.new_seats(50)
		"""
		if not isinstance(number_of_new_seats, int):
			raise TypeError("Количество новых посадочных мест должно быть типа int")
		if number_of_new_seats <= 0:
			raise ValueError("Количество новых посадочных мест должно быть положительным числом")
		...


class BuilderMan:
	def __init__(self, age: int, specialisations: list[str], have_higher_education: bool):
		'''
		Создание и подготовка к раоте объекта "Строитель"
		:param age: Возраст строителя
		:param specialisations: Специализации строител
		:param have_higher_education: Наличие высшего образования

		Примеры:
		>>> builderman_1 = BuilderMan(35, ["Бетонщик", "Арматурщик"], False)
		'''
		if not isinstance(age, int):
			raise TypeError("Возраст должен быть типа int")
		if age <= 18:
			raise ValueError("К работе на стройке допускаются только совершеннолетние")
		self.age = age

		if not isinstance(specialisations, list):
			raise TypeError("Специализации сотрудника подаются в виде списка типа list")
		self.specialisations = specialisations

		if not isinstance(have_higher_education,  bool):
			raise TypeError("Информация о наличии высшего образования должна быть типа bool")
		self.have_higher_education = have_higher_education

	def get_new_specialisation(self, specialisation: str) -> None:
		'''
		Функция которая добавляет новую специализацию строителю

		:param specialisation: Новая специализация строителя

		Примеры:
		>>> builderman_1 = BuilderMan(35, ["Бетонщик", "Арматурщик"], False)
		>>> builderman_1.get_new_specialisation("Сварщик")
		'''
		if not isinstance(specialisation, str):
			raise TypeError("Специализация должна быть типа str")
		...
	def celebrate_birthday(self) -> None:
		'''
		Функция которая добавляет 1 год к возрасту строителя

		Примеры:
		>>> builderman_1 = BuilderMan(35, ["Бетонщик", "Арматурщик"], False)
		>>> builderman_1.celebrate_birthday()
		'''

		...
	def can_be_foreman(self) -> bool:
		'''
		Функция определяет может ли строитель стать прорабом по наличию у него определенных
		специализаций, таких как "Арматурщик", "Бетонщик", "Сварщик", а также при наличии
		высшего образования

		:return: Может стать прорабом или нет

		Примеры:
		>>> builderman_1 = BuilderMan(35, ["Бетонщик", "Арматурщик"], False)
		>>> builderman_1.can_be_foreman()
		'''
		...


if __name__ == "__main__":
    doctest.testmod()
