from pprint import pprint


def convert_to_dict():
    representation_list = [{'bin': bin(number), 'dec': number, 'hex': hex(number), 'oct': oct(number)} for number in range(0, 16)]
    return representation_list


pprint(convert_to_dict())