#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program02 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"
# python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program01 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"
# python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program01 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"
def most_frequent_chars(filename: str) -> str:
    def analyzer(ws):
        lenght = len
        max_len, len_ws = lenght(max(ws, key=len)), lenght(ws)-1
        two_d, count = [{} for i in range(max_len)], {}

        for position, word in zip(range(len_ws+1), ws):
            lenght_word, index = lenght(word), 0
            while index < lenght_word:
                letter = word[index]
                if two_d[index][letter] is True:
                        if lenght_word-1 > index and two_d[index+1][word[index+1]] is True:
                            letter = word[index+3]
                        else:
                            letter = word[index+1]


                current = two_d[index][letter] = two_d[index].get(letter, 0) + 1
                if current > count[index][0] or (letter < count[index][1] and current == count[index][0]):
                    count[index] = (current, letter)

                if count[index][0] - current > len_ws-position:
                    current = True
                if lenght_word-1 > index and two_d[index+1][word[index+1]] is True:
                    index += 1
                index += 1

        return "".join(x[1] for x in count.values())


    nxt,  workspace = filename, []
    while True:
        workspace = open(nxt, "r", encoding="utf8").read().split() + workspace
        nxt = workspace.pop(0)

        if nxt == filename:
            return analyzer(tuple(workspace))


if __name__ == "__main__":
    # print(most_frequent_chars('test03/woodchuck.txt'))
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
    for key, value in datas:
        most = most_frequent_chars(key)
        print(f"{most}\n{value}\n{most == value}")
    pass
