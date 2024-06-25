calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return string, string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    strings = string.upper()
    for i in list_to_search:
        if strings == i.upper():
            return True
        elif strings != i.upper():
            return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)