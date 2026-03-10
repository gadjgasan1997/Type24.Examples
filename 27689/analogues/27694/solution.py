# Читаем строку из файла
s = open("data.txt").readline()

current_length = 0  # Текущая длина правильной цепочки
max_length = 0  # Рекордная длина
next_expected_char = 'A'  # Символ, который мы ждем следующим

for char in s:
    # Если пришел именно тот символ, который мы ждали
    if char == next_expected_char:
        current_length += 1
        max_length = max(max_length, current_length)

        # Определяем, какой символ будет следующим в очереди
        if char == 'A':
            next_expected_char = 'B'
        else:  # если char == 'B'
            next_expected_char = 'A'

    # Если пришел не тот символ, но это 'A' — начинаем новую цепочку с него
    elif char == 'A':
        current_length = 1
        next_expected_char = 'B'

    # Если пришел не тот символ и это не 'A' — всё сбрасывается
    else:
        current_length = 0
        next_expected_char = 'A'

print(max_length)