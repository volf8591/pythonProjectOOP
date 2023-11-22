STATUS_CONTINUE = 'Игра продолжается'
EMPTY = '_'
ROW1 = '1'
ROW2 = '2'
ROW3 = '3'
COLA = 'a'
COLB = 'b'
COLC = 'c'
data = {
    ROW1: {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY,
    },
    ROW2: {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY,
    },
    ROW3: {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY,
    }
}
alowed_symbols = ['X', 'O']
alowed_rows = [ROW1, ROW2, ROW3]
alowed_cols = [COLA, COLB, COLC]

def check_is_game_end():
    winner = STATUS_CONTINUE

    empty_symbols = 0
    for dat in data.values():
        for d in dat.values():
            if d == EMPTY:
                empty_symbols += 1

    # Условие победы по строкам
    if (data[ROW1][COLA] == data[ROW1][COLB]) and (data[ROW1][COLA] == data[ROW1][COLC]) and (data[ROW1][COLA] != EMPTY):
        winner = data[ROW1][COLA]
    elif (data[ROW2][COLA] == data[ROW2][COLB]) and (data[ROW2][COLA] == data[ROW2][COLC]) and (data[ROW2][COLA] != EMPTY):
        winner = data[ROW2][COLA]
    elif (data[ROW3][COLA] == data[ROW3][COLB]) and (data[ROW3][COLA] == data[ROW3][COLC]) and (data[ROW3][COLA] != EMPTY):
        winner = data[ROW3][COLA]

    # Условие победы по колонкам
    elif (data[ROW1][COLA] == data[ROW2][COLA]) and (data[ROW1][COLA] == data[ROW3][COLA]) and (
            data[ROW1][COLA] != EMPTY):
        winner = data[ROW1][COLA]
    elif (data[ROW1][COLB] == data[ROW2][COLB]) and (data[ROW1][COLB] == data[ROW3][COLB]) and (data[ROW1][COLB] != EMPTY):
        winner = data[ROW1][COLB]
    elif (data[ROW1][COLC] == data[ROW2][COLC]) and (data[ROW1][COLC] == data[ROW3][COLC]) and (data[ROW1][COLC] != EMPTY):
        winner = data[ROW1][COLC]
        # Условия победы по диагоналям
    elif (data[ROW1][COLA] == data[ROW2][COLB]) and (data[ROW1][COLA] == data[ROW3][COLC]) and (data[ROW1][COLA] != EMPTY):
        winner = data[ROW1][COLA]
    elif (data[ROW1][COLC] == data[ROW2][COLB]) and (data[ROW1][COLC] == data[ROW3][COLA]) and (
            data[ROW1][COLC] != EMPTY):
        winner = data[ROW1][COLC]
    # Все ячейки заполнены, но победа не обнаружена:
    elif empty_symbols == 0:
        winner = 'Ничья'

    return winner
def input_value(input_value, value):
    column = input_value[1].lower()
    if column not in alowed_cols:
        return (f'[?] Вы ввели не верную колонку: {column}. Разрешенные колонки: {alowed_cols} Вы потеряли ход')

    row = input_value[0]
    if row not in alowed_rows:
        return (f'[?] Вы ввели не верную строку: {row}. Разрешенные строки: {alowed_rows} Вы потеряли ход')

    if value in alowed_symbols and data[row][column] == EMPTY:
        data[row][column] = value
        return 'Ход принят'
    else:
        return(f'[?] Вы потяряли ход, так как использовали запрещенный символ {value}, разрешенные символы: {alowed_symbols}, или ячейка уже заполнена')
    pass
def print_game_field():
    str_result = 'Данные вводятся в формате : 1a\n'
    str_result += f" \t\ta\t\tb\t\tc\n"
    str_result += f"1\t\t{data[ROW1][COLA]}\t\t{data[ROW1][COLB]}\t\t{data[ROW1][COLC]}\n"
    str_result += f"2\t\t{data[ROW2][COLA]}\t\t{data[ROW2][COLB]}\t\t{data[ROW2][COLC]}\n"
    str_result += f"3\t\t{data[ROW3][COLA]}\t\t{data[ROW3][COLB]}\t\t{data[ROW3][COLC]}\n"

    return str_result


def clear_data():
    data[ROW1] = {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY
    }
    data[ROW2] = {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY
    }
    data[ROW3] = {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY
    }




