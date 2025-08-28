# Функция reverse, которую вы хотите протестировать
def reverse(string):
    return string[::-1]

# Читаем входные данные из файла
with open('input.txt', 'r') as file:
    input_text = file.read()

# Читаем ожидаемый результат
with open('expected_output.txt', 'r') as file:
    expected_output = file.read()

# Используем функцию и проверяем результат
actual_output = reverse(input_text)

# Проверяем совпадает ли результат с ожидаемым
if actual_output == expected_output:
    print("Тест пройден")
else:
    print("Тест не пройден")