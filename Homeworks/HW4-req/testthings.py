#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program02 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"
# python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program01 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"
# python -u -m timeit -v -v -v -v -n 5  -r 3  -s "from program01 import most_frequent_chars" "most_frequent_chars('test01/A.txt')"
def most_frequent_chars(filename: str) -> str:
    def load_files():
        nxt, dups, uniq = filename, {}, set()
        frequencies, count = [], {}
        while True:
            nxt, *file = open(nxt, "r", encoding="utf8").read().split()
            for word in file:
                if word in uniq:
                    try:
                        dups[word] += 1
                    except KeyError:
                        dups[word] = 1
                else:
                    uniq.add(word)
                    index = 0
                    for letter in word:
                        try:
                            frequencies[index][letter] += 1
                        except KeyError:
                            frequencies[index][letter] = 1
                        except IndexError:
                            frequencies.append({letter:1})
                        try:
                            if frequencies[index][letter] > frequencies[index][count[index]] or (letter < count[index] and frequencies[index][letter] == frequencies[index][count[index]]):
                                count[letter] = letter
                        except KeyError:
                            count[index] = letter
                        index += 1


            if nxt == filename:
                return dups, count

    dups, old_count = load_files()
    new_count, frequencies = {}, []
    if not len(dups):
        return "".join(old_count.values())
    for letters, occurrence in dups.items():
        index = 0
        for letter in letters:
            frequencies[index][letter] += occurrence

            try:
                if frequencies[index][letter] > frequencies[index][count[index]] or (letter < count[index] and frequencies[index][letter] == frequencies[index][count[index]]):
                    count[index] = letter
            except KeyError:
                count[index] = letter

            index += 1


    return "".join(count.values())

if __name__ == "__main__":
    # print(most_frequent_chars("test08/boilings.txt"))
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
