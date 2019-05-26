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
    zhang_an =  pinyin('張婉瑜', style=Style.BOPOMOFO)
    xu_an = pinyin('許陳明', style=Style.BOPOMOFO)
    yang_an = pinyin('楊勝安', style=Style.BOPOMOFO)
    lu_an = pinyin('劉伊珊', style=Style.BOPOMOFO)

dict = {0: '劉懿珊', 1: '楊森安', 2: '許成名', 3: '陳國熏',
        4: '張莞渝', 5: '馮文瑋', 6: '林曉郁', 7: '蘇雍順', 8: '張莞渝', 9: '許成名',10:'楊森安'
        ,11:'劉懿珊'}


def compaere_name(input_name):
    a = [e.value for e in InputType]
    # print(a)
    text = pinyin(input_name, style=Style.BOPOMOFO)
    try:
        a.index(text)
        num = a.index(text)
        return dict[num]
    except ValueError:
        #return 2
        return False


kf = compaere_name('許陳明')
print(kf)
print(dict[8])
