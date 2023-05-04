import json
import datetime
from operator import itemgetter



def encave_numbers(volue: str):
    open_number = volue.split(' ')
    if len(open_number[-1]) == 16:
        open_number[-1] = open_number[-1][:4] + ' ' + open_number[-1][4:6] + '** **** ' + open_number[-1][12:]
    elif len(open_number[-1]) == 20:
        open_number[-1] = '**' + open_number[-1][16:]
    else:
        open_number[-1] = 'None'
    return ' '.join(open_number)


def latter_5_operations(data: list):
    data_sorted = []

    for item in data:
        if 'date' in item:
            if item['state'] == 'EXECUTED':
                item['date'] = datetime.datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f')
                data_sorted.append(item)

    sorted(data_sorted, key=itemgetter('date'), reverse=True)
    result = ''
    for x in range(6):

        if 'from' not in data_sorted[x]:
            data_sorted[x]['from'] = 'None'
        result += f"\n{data_sorted[x]['date'].strftime('%d.%m.%Y')} {data_sorted[x]['description']}\n" \
            f"{encave_numbers(data_sorted[x]['from'])} -> {encave_numbers(data_sorted[x]['to'])}\n" \
            f"{data_sorted[x]['operationAmount']['amount']} {data_sorted[x]['operationAmount']['currency']['name']}\n"
    return result

if __name__ == '__main__':
    file = open('operations.json')
    data = json.load(file)
    print(latter_5_operations(data))




