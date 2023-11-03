# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

dishes = ["A","B","C","D","E","F","G"]
message_num = get_number()
for i in range(message_num):
    message = input()
    message = message.upper()
    max_letter = ""
    max_count = 0
    for letter in dishes:
        count = message.count(letter)
        if count > max_count:
            max_count = count
            max_letter = letter
    print(max_letter)
    
    