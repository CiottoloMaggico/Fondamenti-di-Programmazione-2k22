#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program02 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"
python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program01 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"
'''


def most_frequent_chars(filename: str) -> str:
    def load_files():
        nxt, res = filename, []
        while True:
            file = open(nxt, "r", encoding="utf8").read().split()
            nxt = file[0]
            res += file[1:]

            if nxt == filename:
                return tuple(res)

    workspace = load_files()
    lenght, maxi = len, max
    max_lenght = lenght(maxi(workspace, key=lenght))
    two_d, count, item = list({} for i in range(max_lenght)), [
        0]*max_lenght, ["a"]*max_lenght

    for i in workspace:
        tuple(two_d[j].update({i[j]: two_d[j].get(i[j], 0) + 1}) for j in range(max_lenght) if len(i) > j)
        
    return "".join([min([j for j in i if i[j] == i[maxi(i, key=i.get)]], key=ord) for i in two_d])


if __name__ == "__main__":
    print(most_frequent_chars("test01/A.txt"))
    pass
