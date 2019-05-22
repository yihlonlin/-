from pypinyin import pinyin, lazy_pinyin, Style
from enum import Enum


class InputType(Enum):

    lu = pinyin('劉懿珊', style=Style.BOPOMOFO)
    yang = pinyin('楊森安', style=Style.BOPOMOFO)
    xu = pinyin('許成名', style=Style.BOPOMOFO)
    chen = pinyin('陳國熏', style=Style.BOPOMOFO)
    zhang = pinyin('張莞渝', style=Style.BOPOMOFO)
    feng = pinyin('馮文瑋', style=Style.BOPOMOFO)
    lin = pinyin('林曉郁', style=Style.BOPOMOFO)
    su = pinyin('蘇雍順', style=Style.BOPOMOFO)


dict = {0: '劉懿珊', 1: '楊森安', 2: '許成名', 3: '陳國熏',
        4: '張莞渝', 5: '馮文瑋', 6: '林曉郁', 7: '蘇雍順'}


def compaere_name(input_name):
    a = [e.value for e in InputType]
    # print(a)
    text = pinyin(input_name, style=Style.BOPOMOFO)
    try:
        a.index(text)
        num = a.index(text)
        return dict[num]
    except ValueError:
        return False


# kf = compaere_name('劉懿珊')
# print(kf)
