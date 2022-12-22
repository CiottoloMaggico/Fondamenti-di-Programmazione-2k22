#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program02 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"
# python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program01 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"
# python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program01 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"
def most_frequent_chars(filename: str) -> str:
    def load_files():
        nxt, dups = filename, {}
        while True:
            nxt, *file = open(nxt, "r", encoding="utf8").read().split()
            for word in file:
                try:
                    dups[word] += 1
                except KeyError:
                    dups[word] = 1

            if nxt == filename:
                return dups

    duples = load_files()
    two_d, count = [], []

    for letters, occurrence in duples.items():
        index = 0
        for letter in letters:
            try:
                two_d[index][letter] += occurrence
            except KeyError:
                two_d[index][letter] = occurrence
            except IndexError:
                two_d.append({letter:occurrence})

            try:
                if two_d[index][letter] > two_d[index][count[index]] or (letter < count[index] and two_d[index][letter] == two_d[index][count[index]]):
                    count[index] = letter
            except IndexError:
                count.append(letter)

            index += 1


    return "".join(count)

if __name__ == "__main__":
    # print(most_frequent_chars('test01/A.txt'))
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
