def custom_write(file_name, strings):
    name = file_name
    bite_num = []
    strings_positions = {}
    file = open(name, 'a', encoding='utf-8')
    for string_file in strings:
        position = file.tell()
        bite_num.append(position)
        file.write(string_file + '\n')
    file.close()
    string_count = 0
    for i in strings:
        strings_positions.update({(string_count, bite_num[string_count]): i})
        string_count += 1
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)