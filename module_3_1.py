calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    length = len(string)
    string_upper = string.upper()
    string_lower = string.lower()
    tuple_string = (length, string_upper, string_lower)
    return tuple_string


def is_contains(string, list_to_search):
    count_calls()
    flag = True
    for i in list_to_search:
        word_ = i.lower()
        string_lower = string.lower()
        if string_lower == word_:
            flag = True
            break
        else:
            flag = False
            continue
    if flag:
        print(True)
    else:
        print(False)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)


