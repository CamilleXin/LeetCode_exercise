# ！usr/bin/env python

__author__ = 'Camille'


def str_no_repeat(str):
    start = maxlength= 0
    usedChar = {}
    length = len(str)
    for i in range(length):
        if str[i] in usedChar and start <= usedChar[str[i]]:
            start = usedChar[str[i]] + 1
        else:
            maxlength = max(maxlength, i - start + 1)
        usedChar[str[i]] = i
    print(maxlength)


if __name__ == '__main__':
    str = "pwwkew"
    str_no_repeat(str)
