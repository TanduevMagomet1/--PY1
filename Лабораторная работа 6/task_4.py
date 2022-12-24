import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    to_json = []
    with open(filename, 'r') as csv:
        data = [[value.strip() for value in raw_line.split(',')] for raw_line in csv.readlines()]  # преобразуем данные из csv файла в список списков
        headers = data[0]
        rows = data[1:]
        for row in rows:
            csv_dict = {}
            for number, value in enumerate(row):
                csv_dict[headers[number]] = value
            to_json.append(csv_dict)
    return(to_json)


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
