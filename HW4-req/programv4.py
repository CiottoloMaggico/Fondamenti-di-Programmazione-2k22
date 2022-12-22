#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program02 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"
# python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program01 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"
# python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program01 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"

def most_frequent_chars(filename: str) -> str:
    def load_files():
        duplicates = {}
        nxt, workspace = filename, []
        while True:
            nxt, *file = open(nxt, "r", encoding="utf8").read().split()
            workspace += file

            if nxt == filename:
                for i in workspace:
                    duplicates[i] = duplicates.get(i, 0) +1
                return set(workspace), {key:value for key, value in duplicates.items() if value > 1}

    ws, duplicates = load_files()
    max_len = lenght(max(workspace, key=lenght))
    two_d, count, final = [{} for i in range(max_len)], [0]*max_len, ""

    for i in ws:
        index = 0
        for j in i:
            two_d[index][j] = two_d[index].get(j, 0) + 1
            if count[index] == 0 or two_d[index][j] > two_d[index][count[index]] or (j < count[index] and two_d[index][j] == two_d[index][count[index]]):
                count[index], final = j, final[:index]+j+final[index+1:]


            index += 1
    return final



if __name__ == "__main__":
    print(most_frequent_chars('test12/incipience.txt'))
    datas = (('test02/bullfight.txt', 'poternusakesness'),
        ('test03/woodchuck.txt', 'aanreeaseesable'),
        ('test04/pampers.txt', 'ceeelieessseds'),
        ('test05/avocados.txt','sereeieeesssssncy'),
        ('test06/strums.txt', 'sereeeeesssssssynssm'),
        ('test07/sinew.txt', 'すひびずじぞぜぃけそみきおょぇどべしこしこれれあねきゞ゜ぷ'),
        ('test08/boilings.txt', '🚏🏞😨♣☢🐸‼🗻🌚🥷🍯🎽♾🗽🍄⚔🫓😠🍈🪀🏞➡🍼👩😻📿🌁🕌👾🤓😚®❇💒🦪👒💂☪🥡🥕'),
        ('test09/meddles.txt', 'ᛢᚦᛝᛡᚤᚬᚬᛍᚸᛘᚣᚢᛜᛥᚳᛜᛖᛄᚢᛊᚬᛟᛈᛅᛞᚹᛯᚼᛁᚺ'),
        ('test10/aileron.txt', 'ᛠᚣᚻᛝᚧᛜ᛭くᚻᛝᚭᛈᚺᛦᚩᛞᛏᚽᛪᚢᚰᚯひᛃだᚯᚨろᚷᚦᛕᚸᛯᛄᛩᛂᚲᛆᛏᚰᛨぼゆᛇᛮᛚᚯᛓやᚼかᚯᚨᛦ᛫ᚩᚲᛋᚽ👘♒ぜ🕋ゔ🕣📬💊☺🦌'),
        ('test11/metonymies.txt', 'ᛃᚬᛝᚸᛈᚦᚱᛦᛢᛮᚼᛋᚯᛤᚳᛈᛓᚿᛊᚬᛈᚯᛎᚦᛅᛮᚧᚬᛦᚲᚮᚶᛑきᛓᛔᛮぞᛘᚼᛤᚩᛮᚼᛋᛛᛡᚱᛌᛑᚩᛪきᛤᛃᛅᛞᛏᛣᚤᚻᚦᚢᚩᛨᛐᛘゔᚷᚴᚧᚺᛖᛑᛨᛈがᛃᛥᚽᛚᚣᛋᚾᚳᚩごばᚩᚰぐがたᚨᚼᚩᛉ゜ᛅᚬᚲぅしᛪᚵᚨぎᛝᛡᛀごでᛟᚸゖそぇが🏟🃏じゔᚫぴ💌🔸😖ᛆᛪᚯ᛫ᚤᛑᚺᚾᛒᛦにぼ゙ぞゃせねねな'),
        ('test12/incipience.txt', 'sereeeeeesssssssりᚷᛈᚳᚽᚿᚪᛙᛪᛄᚩᚿᛨᚧᚮめわᛂᛆᛘᛤᛤᛜᛉᛈᚣのぽᚳᛅᚺᛊᛛᚪᚶᚡᛘᚷᚥᛑ᛬ᛋᚥᚩᚮᛏᛅᛎᚯᚱᚽしᚻᛔᚳᛇᚪᛅᚲᚪᛨᛒゐᚨᚰᚽᚩᚿつげᛊつᚢだᛇᚺᛯᚮりᚬᚴᚹよょぬおᚱᛮᛏᚹᛑᚮっᛋ🛢ᚲᛢ📲ぃᚭᛡゐぴ🆖🫒⏰👹🍹ᛅ⏏◀🛄👍🌽🔥🎅🆙🦒🦟🔤🚓😗😕ᛦᛃᛮᛈᛂ'),)
    # for key, value in datas:
    #     most = most_frequent_chars(key)
    #     print(f"{most}\n{value}\n{most == value}")
    pass
