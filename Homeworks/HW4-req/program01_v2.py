#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program02 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"
# python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program01 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"
# python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program01_v2 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"

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
        for j in range(max_lenght):
            if lenght(i) <= j:
                break
            else:
                two_d[j][i[j]] = two_d[j].get(i[j], 0) + 1

                if two_d[j][i[j]] > count[j] or (i[j] < item[j] and two_d[j][i[j]] == count[j]):
                    count[j], item[j] = two_d[j][i[j]], i[j]

    return "".join(item)


if __name__ == "__main__":
    print(most_frequent_chars("test01/A.txt"))
    pass
