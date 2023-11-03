 # a simple parser for python. use get_number() and get_word() to read
import pprint


def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


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

def check_if_in_sequence_all(string_1, string_2):
    continue_it = True
    while True:
        continue_it = False
        for i in range(num_seq):
            # for each sequence
            single_series_seq = sequences.get(i)
            for single_seq_element in single_series_seq:
                start_index = string_1.find(single_seq_element)
                if start_index != -1:
                    suffix_1 = string_1[start_index + len(single_seq_element):]
                    seq_new = string_2[start_index : len(string_2) - len(suffix_1) ]
                    for single_seq_element_2 in single_series_seq:
                        if single_seq_element_2 in seq_new:
                            # check prefix
                            if string_1[:start_index] == string_2[:start_index]:
                                return (True, start_index, i, len(suffix_1))
        # check if the prefex are equa in the two strings letter by letter

        while True:
            if string_1[0] == string_2[0]:
                string_1 = string_1[1:]
                string_2 = string_2[1:]
                continue_it = True
            else :
                break
        if not continue_it:
            return (False, 0, 0, 0)
                
        




global num_seq
num_seq = get_number()
global sequences
sequences = {}

for i in range(num_seq):
    seq = input()
    sequence = seq.split(" ")
    sequences[i] = sequence[1:]

set_sequences = set()
for i in range(num_seq):
    single_series_seq = sequences.get(i)
    for single_seq_element in single_series_seq:
        set_sequences.add(single_seq_element)


test_case = get_number()

for test in range(test_case):
    test_seq = input()
    test_sequence = test_seq.split(" ")
    old_pass = test_sequence[0]
    new_pass = test_sequence[1]
    if old_pass == new_pass:
        print("REJECT")
        continue

    # remove the same initial letter in the password and new password
    (match, start_index, seq_index, suffix) = check_if_in_sequence_all(old_pass, new_pass)

    if match:
        old_suffix = old_pass[len(old_pass) - suffix:]
        new_suffix = new_pass[len(new_pass) - suffix:]
        if old_suffix == new_suffix:
            print("REJECT")
            continue
        else:
            # iterate while the suffix is empty
            while True:
                if len(old_suffix) == 0:
                    #todo
                    break
                else:
                    # check the letter before the suffix
                    old_prefix = old_pass[:len(old_pass) - suffix ]
                    new_prefix = new_pass[:len(new_pass) - suffix ]
                    if old_prefix == new_prefix:
                        (match_2, start_index_2, seq_index_2, suffix_2) = check_if_in_sequence_all(old_suffix, new_suffix)
                        if not match_2:
                            print("OK")
                            break
                        else:
                            old_suffix = old_suffix[len(old_suffix) - suffix_2:]
                            new_suffix = new_suffix[len(new_suffix) - suffix_2:]
                            if old_suffix == new_suffix:
                                print("REJECT")
                                break  
                            else :
                                continue
                    else:
                        print("OK")
                        break
    else:
        print("OK")
        continue
