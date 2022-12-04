def delete(list_, index=None):
    # функция реализована без использования синтаксиса отрицательных индексов в слайсировании
    if index is None:
        list_ = list_[:len(list_) - 1]  # берем срез списка без последнего элемента
    else:
        if index < 0:  # если индекс отрицательный, то переводим его в положительный
            index = len(list_) + index
        list_before = list_[:index]  # создаем список элементов до переданного индекса
        list_after = list_[index + 1:]  # создаем список элементов после переданного индекса
        list_ = list_before + list_after  # соединяем списки для получения результата
    return list_

print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
