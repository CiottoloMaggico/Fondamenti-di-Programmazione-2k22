import random
from program01 import decode_XKCD_tuple, decode_value


CHOICE = ["1","5","10","50","100","500","1000"]
LENGHT_TUPLE = 1000
MAX_LENGHT_ITEM = 10

final_test = []
for i in range(LENGHT_TUPLE):
    current = ""
    while len(current) < random.randint(2, MAX_LENGHT_ITEM):
        choice = random.choice(CHOICE)
        current += choice
        last = len(choice)
        if decode_value(current) > 3999:
            current = current[:-last]
        
    final_test += [current]


k = random.randint(0, len(final_test))
expected = decode_XKCD_tuple(final_test, k)
        
with open("test_case.txt", "a") as text_file:
    text_file.write(f"{str(final_test)} {k}\n{expected}\n\n")
text_file.close()