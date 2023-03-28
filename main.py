# Введіть ключове слово, за яким будуть відбиратись рядки
keyword = input("Введіть ключове слово: ")

# Відкрийте вихідний файл для запису відфільтрованих рядків
with open("filtered.txt", "w") as output_file:

    # Відкрийте вхідний файл для читання
    with open("input.txt", "r") as input_file:

        # Перебирайте кожен рядок вхідного файлу
        for line in input_file:

            # Якщо рядок містить ключове слово, то додайте його до вихідного файлу
            if keyword in line:
                output_file.write(line)
