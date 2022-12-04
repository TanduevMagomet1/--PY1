def delete(list_, index=None):
    if index is None:
        list_ = list_[:-1]  # берем срез списка без последнего элемента
    else:
        if index < 0:  # если индекс отрицательный, то переводим его в положительный
            index = len(list_) + index
        list_ = list_[:index] + list_[index + 1:]  # соединяем списки для получения результата
    return list_

print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
