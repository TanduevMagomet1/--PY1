class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        print("Данное значение нельзя менять")
        return

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, new_author):
        print("Данное значение нельзя менять")
        return

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise ValueError("Количество страниц должно быть целым числом")
        self.__pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int):
            raise ValueError("Количество страниц должно быть целым числом")
        self.__pages = pages

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise ValueError("Длительность должна быть числом с плавающей запятой")
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, float):
            raise ValueError("Длительность должна быть числом с плавающей запятой")
        self.__duration = duration

